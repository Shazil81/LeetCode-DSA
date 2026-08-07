class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap + sorting : Not Optimal
        res = []
        n = len(nums)

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Top K elements ko result list me daalna
        result = []
        for i in range(k):
            result.append(sorted_items[i][0]) # sorted_items[i][0] se number milega
            
        return result