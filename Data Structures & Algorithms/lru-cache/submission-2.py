"""
if you can't use ordereddict you can just use a node class
class Node:
    def __init__(self, key=0, value=0):
        # Stores the lookup key (needed to delete from the dict during eviction)
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# remove leftmost for oldest, moving to rightmost represents most recent.
# each node must store key so when you remove the node you can use the key
# to remove the cache hashmap entry.
"""

# in custom node implementation, use two dummy nodes for base head and tail incase the 
# cache is empty.

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity

        self.pointerMap = OrderedDict()



    def get(self, key: int) -> int:
        if key in self.pointerMap:
            # put to rightmost of the ordered dict
            self.pointerMap.move_to_end(key)
            return self.pointerMap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.pointerMap:
            self.pointerMap.move_to_end(key)
        self.pointerMap[key] = value
        if len(self.pointerMap) > self.size:
            self.pointerMap.popitem(last=False)