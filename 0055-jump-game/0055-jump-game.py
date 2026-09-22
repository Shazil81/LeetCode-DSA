class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # hai ye greedy algorithm pe based hai
        farthest = 0
        for i in range(len(nums)):
            # jab i bada ho jayega ka mtlb hai ki mera aage badh nhi payega tb hi to i bada ho gya farthest se
            if i > farthest:
                return False
            # agar i bada nhi h to farthest ko update kr denge kyun ki i+nums[i] btayega ki kitna dur ja skte hain
            farthest = max(farthest, i+nums[i])

        return True