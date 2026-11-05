class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        i = 0
        # Charhayi
        while i+1 < n and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == n-1:
            return False
        
        # Utrayi
        while i+1 < n and arr[i] > arr[i+1]:
            i += 1
        
        return i == n-1 # end tak phunch gye mtlb ki decrease hoga or increase hoga to i to badhega hi na or last tk jayega agar nhi gya last tk yaani khi pe equal hai