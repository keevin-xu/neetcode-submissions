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