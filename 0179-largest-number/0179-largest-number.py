from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        str_nums = list(map(str, nums))

        def compare(a, b):  # agar string a + b ya b + a ko jorne jo bada aaye wo aage hoga isi liye comparator wala sort use krna pada
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        str_nums.sort(key=cmp_to_key(compare))

        if str_nums[0] == '0': # agar "00" aisa case hai to 
            return "0"
        
        return "".join(str_nums)