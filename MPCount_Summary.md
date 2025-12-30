# MPCount: Single Domain Generalization for Crowd Counting

## Repository Overview

**MPCount** is a PyTorch implementation of a state-of-the-art crowd counting model presented at CVPR 2024. The repository addresses the challenging problem of **Single Domain Generalization (SDG)** in crowd counting, where a model trained on one dataset must generalize well to unseen datasets with different characteristics.

**Paper**: [Single Domain Generalization for Crowd Counting](https://arxiv.org/pdf/2403.09124.pdf)  
**Repository**: https://github.com/Shimmer93/MPCount  
**Conference**: CVPR 2024

### Key Problem
Traditional crowd counting models often suffer from domain shift - they perform well on the training dataset but poorly on different datasets with varying crowd densities, perspectives, and imaging conditions. MPCount solves this by learning domain-invariant representations from a single source domain.

---

## Model Architecture

### Core Components

MPCount uses a **VGG16-BN** based encoder-decoder architecture with several innovative modules:

#### 1. **Backbone Encoder (VGG16-BN)**
- **enc1**: First 23 layers of VGG16-BN (outputs 256 channels)
- **enc2**: Layers 23-33 (outputs 512 channels)
- **enc3**: Layers 33-43 (outputs 512 channels)

The encoder extracts hierarchical feature representations at multiple scales.

#### 2. **Decoder Network**
Three decoder blocks with skip connections:
- **dec3**: 512 → 1024 → 512 channels
- **dec2**: 1024 → 512 → 256 channels (concatenates upsampled dec3 with enc2)
- **dec1**: 512 → 256 → 128 channels (concatenates upsampled dec2 with enc1)

#### 3. **Memory Module**
The key innovation for domain generalization:
```python
mem = nn.Parameter(torch.FloatTensor(1, mem_dim, mem_size))
# Default: mem_dim=256, mem_size=1024
```

**Purpose**: Creates a learnable memory bank that stores prototypical patterns across domains.

**Operation**:
1. Computes attention weights between feature maps and memory bank
2. Retrieves relevant memory patterns using soft attention
3. Produces domain-invariant features

**Mathematical formulation**:
```
logits = (M^T × Y) / √k
Y_new = M × softmax(logits)
```
where M is the memory bank, Y is the feature map, and k is the feature dimension.

#### 4. **Classification Head**
Predicts a binary mask indicating crowd/non-crowd regions:
- Input: 512 channels from enc3
- Architecture: Conv(512→256) → Dropout → Conv(256→1) → Sigmoid
- Output: Binary map (downsampled by 16×)
- Purpose: Filters out regions without people to improve accuracy

#### 5. **Density Map Head**
Generates the final crowd density map:
- Input: 256-dim memory-augmented features
- Architecture: Conv(256→1)
- Output: Density map that, when integrated, gives the crowd count

---

## Pipeline Overview

### Training Pipeline

The training pipeline consists of multiple stages with progressive complexity:

#### **Mode: 'final'** (Complete Pipeline)

This is the most advanced training mode that combines all components.

**Input Preparation**:
1. Load paired images: `(img1, img2)` - two augmented versions of the same scene
2. Ground truth data: `(density_maps, crowd_points, classification_maps)`
3. Apply data augmentation (crops, flips, color jittering)
4. Normalize images: mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]

**Forward Pass Steps**:

```
For img1 and img2:
│
├─► 1. Feature Extraction (forward_fe)
│     ├─ Pass through VGG encoder (enc1, enc2, enc3)
│     ├─ Decode with skip connections (dec3, dec2, dec1)
│     └─ Output: multi-scale features (y_cat) + deep features (x3)
│
├─► 2. Dense Feature Processing (den_dec)
│     ├─ Reduce channels: y_cat → 256-dim features
│     └─ Output: y_den1, y_den2
│
├─► 3. Consistency Regularization
│     ├─ Normalize features: y_in = InstanceNorm(y_den)
│     ├─ Compute error: e = |y_in1 - y_in2|
│     ├─ Generate mask: e_mask = (e < err_thrs)  # err_thrs=0.5
│     └─ Mask and dropout: y_masked = Dropout(y_den * e_mask)
│
├─► 4. Memory Augmentation (forward_mem)
│     ├─ Compute attention: logits = M^T × y_masked / √k
│     ├─ Retrieve patterns: y_new = M × softmax(logits)
│     ├─ Consistency loss: L_con = MSE(softmax(logits1), softmax(logits2))
│     └─ Output: memory-augmented features
│
├─► 5. Classification Branch
│     ├─ Input: deep features x3
│     ├─ Predict: c = Sigmoid(cls_head(x3))
│     ├─ Binarize: c_binary = (c >= 0.5) ? 1 : 0
│     ├─ Compute error: c_err = |c_binary1 - c_binary2|
│     └─ Combine: c_final = clip(c_gt + c_err, 0, 1)
│
├─► 6. Density Map Generation
│     ├─ Generate maps: d = den_head(y_new)
│     ├─ Apply classification mask: dc = d × c_final
│     ├─ Upsample 4×: dc_final = upsample(dc)
│     └─ Output: final density maps (dc1, dc2)
│
└─► 7. Loss Computation
      ├─ Density Loss: L_den = MSE(dc1, gt_dmap) + MSE(dc2, gt_dmap)
      ├─ Classification Loss: L_cls = BCE(c1, c_gt) + BCE(c2, c_gt)
      ├─ Consistency Loss: L_con = MSE(softmax(logits1), softmax(logits2))
      └─ Total Loss: L_total = L_den + 10×L_cls + 10×L_con
```

**Key Training Features**:

1. **Paired Image Training**: Uses two augmented views of the same image to learn robust features
2. **Consistency Regularization**: Enforces similar memory attention patterns between augmented views
3. **Error-based Masking**: Focuses memory module on reliable feature regions (where augmentations agree)
4. **Multi-task Learning**: Jointly optimizes density estimation and crowd classification
5. **Log Transformation**: Ground truth density maps are scaled by `log_para=1000` for numerical stability

**Optimization**:
- Optimizer: AdamW (lr=0.001, weight_decay=0.0001)
- Scheduler: OneCycleLR
- Batch size: 16
- Epochs: 180-300
- Patch size: 320×320 (training crops)

### Inference Pipeline

**Input Processing**:
```
Input Image
│
├─► 1. Preprocessing
│     ├─ Convert to RGB
│     ├─ Resize to multiple of unit_size (default: 16)
│     ├─ Pad if necessary
│     ├─ Normalize: mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]
│     └─ Convert to tensor (1×3×H×W)
│
├─► 2. Patch-based Processing (if image too large)
│     ├─ If H or W >= patch_size (default: 3584):
│     │   ├─ Divide image into patches
│     │   ├─ Process each patch independently
│     │   └─ Aggregate results
│     └─ Else: process entire image
│
├─► 3. Model Forward Pass
│     ├─ Feature extraction (encoder-decoder)
│     ├─ Memory augmentation
│     ├─ Classification prediction
│     ├─ Density map generation
│     └─ Output: density_map (1×1×H×W)
│
├─► 4. Count Estimation
│     ├─ Sum density map: total_density = Σ density_map
│     ├─ Scale back: count = total_density / log_para
│     └─ Output: predicted crowd count
│
└─► 5. Visualization (optional)
      ├─ Display original image
      ├─ Show density heatmap
      └─ Print predicted count
```

**Inference Command**:
```bash
python inference.py \
    --img_path [path/to/image] \
    --model_path [path/to/weights.pth] \
    --save_path results.txt \
    --vis_dir visualizations/
```

---

## Key Innovations

### 1. **Memory-Augmented Feature Learning**
- Learns a dictionary of domain-invariant prototypes
- Retrieves relevant patterns via attention mechanism
- Reduces dependency on domain-specific features

### 2. **Consistency Regularization**
- Enforces similar memory attention for augmented views
- Uses instance normalization for domain-invariant comparison
- Masks unreliable regions based on feature discrepancy

### 3. **Joint Classification & Counting**
- Crowd/non-crowd classification filters false positives
- Especially helpful in complex scenes with background clutter
- Improves precision by masking non-crowd regions

### 4. **Error-Based Sample Selection**
- Identifies reliable feature regions: |IN(feat1) - IN(feat2)| < threshold
- Focuses learning on consistent, generalizable patterns
- Ignores augmentation-sensitive features

### 5. **Deterministic Implementation**
- Fixes non-deterministic behavior of F.interpolate
- Uses FixedUpsample module with learnable kernels
- Ensures fully reproducible results

---

## Datasets

### Supported Datasets

1. **ShanghaiTech Part A (STA)**
   - 482 images with 241,677 annotated people
   - High density crowds (avg: ~501 people/image)
   - Varied perspectives and scenes

2. **ShanghaiTech Part B (STB)**
   - 716 images with 88,488 annotated people
   - Medium density crowds (avg: ~124 people/image)
   - More uniform street scenes

3. **UCF-QNRF**
   - 1,535 images with 1,251,642 annotated people
   - Extreme density variation (49-12,865 people/image)
   - Most challenging dataset

### Data Preprocessing

```bash
# Step 1: Preprocess images and annotations
python utils/preprocess_data.py \
    --dataset sta \
    --origin-dir [ShanghaiTech_path]/part_A \
    --data-dir data/sta

# Step 2: Generate ground truth density maps
python utils/dmap_gen.py --path data/sta
```

**Density Map Generation**:
- Uses Gaussian kernels centered at each person location
- Adaptive kernel size based on local crowd density
- Maps are log-transformed (×1000) for stable training

---

## Performance Results

### Cross-Dataset Generalization (CVPR 2024 Paper)

Training on one dataset, testing on others:

| Source | Target B (MAE/MSE) | Target Q (MAE/MSE) | Target A (MAE/MSE) |
|--------|-------------------|-------------------|-------------------|
| **A**  | 11.4 / 19.7      | 115.7 / 199.8    | -                 |
| **B**  | -                | 165.6 / 290.4    | 99.6 / 182.9      |
| **Q**  | 12.3 / 24.1      | -                | 65.5 / 110.1      |

**Deterministic Version** (New, Fully Reproducible):
| Source | Target B (MAE/MSE) | Target Q (MAE/MSE) |
|--------|-------------------|-------------------|
| **A**  | 11.2 / 20.0      | 112.8 / 193.8    |

**Key Achievement**: Exceptional generalization with minimal performance loss compared to domain-specific training.

---

## Model Variants

The repository includes several model variants for ablation studies:

1. **DGModel_base**: Baseline encoder-decoder without domain generalization
2. **DGModel_mem**: Adds memory module only
3. **DGModel_memadd**: Memory + consistency regularization
4. **DGModel_cls**: Baseline + classification head
5. **DGModel_memcls**: Memory + classification
6. **DGModel_final**: Complete model (memory + consistency + classification)

---

## Usage Guide

### Installation

```bash
# Requirements
Python 3.10.12
PyTorch 2.0.1
torchvision 0.15.2

# Install dependencies
pip install -r requirements.txt
```

### Training

```bash
python main.py --task train --config configs/sta_train.yml
```

**Configuration Parameters** (sta_train.yml):
```yaml
seed: 2023
device: 'cuda:0'
log_para: 1000        # Density map scaling factor
patch_size: 10000     # Max patch size for inference
num_epochs: 180
model:
  name: 'final'
  params:
    mem_size: 1024    # Memory bank size
    mem_dim: 256      # Memory feature dimension
    cls_thrs: 0.5     # Classification threshold
    err_thrs: 0.5     # Consistency error threshold
    den_dropout: 0.5  # Density dropout rate
    cls_dropout: 0.3  # Classification dropout rate
```

### Testing

```bash
# Test on target domain
python main.py --task test --config configs/sta_test_stb.yml
```

### Inference on Custom Images

```bash
python inference.py \
    --img_path images/ \
    --model_path weights/model.pth \
    --save_path predictions.txt \
    --vis_dir visualizations/ \
    --patch_size 3584 \
    --log_para 1000
```

---

## Technical Highlights

### Deterministic Training
- Replaces `F.interpolate` with `FixedUpsample`
- Uses learnable upsampling kernels
- Ensures bit-exact reproducibility across runs

### Memory Efficiency
- Patch-based inference for large images
- Processes patches independently, aggregates counts
- Adjustable patch size based on GPU memory

### Data Augmentation Strategy
- Random crops (320×320)
- Horizontal flipping
- Color jittering
- Paired augmentation for consistency learning

### Loss Weighting
- Density loss: 1.0
- Classification loss: 10.0
- Consistency loss: 10.0

The higher weights on auxiliary losses emphasize learning domain-invariant and crowd-aware representations.

---

## Research Contributions

1. **First work** to address single domain generalization in crowd counting
2. **Memory-augmented architecture** for learning domain-invariant features
3. **Consistency regularization** technique using paired augmentations
4. **Joint optimization** of counting and classification for better generalization
5. **Strong empirical results** with significant improvements over baselines

---

## Citation

```bibtex
@inproceedings{pengMPCount2024,
  title = {Single Domain Generalization for Crowd Counting},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024)},
  author = {Peng, Zhuoxuan and Chan, S.-H. Gary},
  year = {2024}
}
```

---

## Repository Structure

```
MPCount/
├── configs/              # Training/testing configuration files
├── datasets/            # Dataset loading and preprocessing
├── models/
│   └── models.py        # All model architectures
├── trainers/
│   ├── trainer.py       # Base trainer class
│   └── dgtrainer.py     # Domain generalization trainer
├── utils/               # Utility functions
├── main.py              # Training/testing entry point
├── inference.py         # Inference script
└── requirements.txt     # Dependencies
```

---

## Pretrained Weights

Available on OneDrive and Google Drive (see README for links).

**Models**:
- Trained on ShanghaiTech A
- Trained on ShanghaiTech B  
- Trained on UCF-QNRF

Each includes both original (non-deterministic) and new (deterministic) versions.

---

## Conclusion

MPCount represents a significant advancement in crowd counting by addressing the critical challenge of domain generalization. Through innovative use of memory modules, consistency regularization, and joint classification-counting, it achieves state-of-the-art cross-dataset performance. The model demonstrates that learning domain-invariant representations from a single source domain is not only possible but can approach the performance of models trained on target domains.

**Key Takeaways**:
- Memory modules enable learning of generalizable prototypes
- Consistency regularization improves robustness to domain shift
- Joint classification-counting enhances precision
- Strong performance across diverse crowd counting benchmarks
