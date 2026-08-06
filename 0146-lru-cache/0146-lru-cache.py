class Node:
    def __init__(self, key=0,value=0):
        """
        :type capacity: int
        """
        self.key=key
        self.value=value
        self.prev=None
        self.next=None 
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache={}
        self.left=Node()
        self.right=Node()
        self.left.next=self.right
        self.right.prev=self.left       

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value
    def insert(self,node):
        prev=self.right.prev
        nxt=self.right
        prev.next=node
        node.prev=prev
        node.next=nxt
        nxt.prev=node
    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.insert(node)
        self.cache[key]=node
        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)