class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([op for op in map(lambda op: 1 if op[1] == '+' else -1, operations)])
