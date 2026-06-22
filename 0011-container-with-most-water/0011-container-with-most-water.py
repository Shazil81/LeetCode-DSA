class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max area nikalna hai ki mera water zyada aaye
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left # width nikala
            # mera jha pe aayega chhota height whi select krna h kyun ki whi decider hai
            h = min(height[left], height[right])
            area = h * width # area ka formula 

            max_area = max(max_area, area) # ab jo area aaya usko max_area se compare kr lia

            if height[left] < height[right]: # agar height mera left wala chhota h to move krenge kyun ki bada krne se koi fayeda nhi h
                left += 1
            else: # or agar right wala mera chhota hai to right ko move kr denge 
                right -= 1
        
        return max_area