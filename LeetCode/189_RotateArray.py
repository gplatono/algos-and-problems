class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) == 0:
            return nums
        total = 0
        for i in range(k % len(nums)):            
            i2 = (k+i) % len(nums)
            fst = i2
            curr = nums[i]
            while total <= len(nums):
                tmp = nums[i2]
                nums[i2] = curr
                curr = tmp
                i2 = (i2 + k) % len(nums)
                total += 1
                if i2 == fst:
                    break
            if total == len(nums):
                break