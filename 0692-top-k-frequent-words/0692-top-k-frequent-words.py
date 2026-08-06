import heapq

class Word:
    def __init__(self, freq, text):
        self.freq = freq
        self.text = text
    
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        
        else:
            return self.text > other.text
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Hashmap + Heap  TC: O(NlogK)  SC: O(N)
        hashmap = {}
        for word in words:
            hashmap[word] = hashmap.get(word, 0) + 1
        
        heap = []
        for word, freq in hashmap.items():
            heapq.heappush(heap, Word(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap).text)
        
        return res[::-1]



