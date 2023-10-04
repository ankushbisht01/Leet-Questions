
class Node():
    def __init__(self , key = -1 , value = -1 , next = None):
        self.key = key 
        self.value = value 
        self.next = next
        

class MyHashMap(object):

    def __init__(self):
        self.map = [Node() for i in range(1000)]
        
        

    def put(self, key, value):
        index = key %1000
        head = self.map[index]
        prev = None
        while(head!=None):
            prev = head 
            if (head.key == key):
                head.value = value 
                return
            head = head.next
        newNode = Node(key , value )
        prev.next = newNode 
        return 
        

    def get(self, key):
        index = key %1000
        head = self.map[index]
        while(head != None):
            if head.key == key:
                return head.value
            head = head.next
        return -1
        

    def remove(self, key):
        index = key % 1000
        curr = self.map[index]
        fast = curr.next 
        while(fast and fast.key != key):
            curr = fast 
            fast = fast.next 
        if (fast):
            curr.next = fast.next 
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)