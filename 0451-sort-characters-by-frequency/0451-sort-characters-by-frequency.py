class Solution:
    def frequencySort(self, s: str) -> str:
       # By using dictionary
       hash_map = {}
       res = ""
       for ch in s:
        hash_map[ch] = hash_map.get(ch, 0) + 1
       
       sorted_chars = sorted(hash_map.items(), key = lambda x : x[1], reverse = True)
       for ch, freq in sorted_chars:
        res = res + (ch*freq)
       return res
