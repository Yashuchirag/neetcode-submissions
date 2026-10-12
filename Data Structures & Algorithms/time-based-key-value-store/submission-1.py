from bisect import bisect_right
from collections import defaultdict

class TimeMap:
    
    def __init__(self):
        self.map_name = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map_name[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        entries = self.map_name.get(key)
        
        if not entries:
            return ""
        i = bisect_right(entries, (timestamp, chr(0x10FFFF)))
        return entries[i - 1][1] if i else ""
