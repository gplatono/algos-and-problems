class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        last_double_idx = 0
        for i in range(len(arr)):
            if arr[i] == 0 and i + count < len(arr) - 1:
                last_double_idx = i
                count += 1
        
        idx = len(arr)-1
        while idx >= 0:
            arr[idx] = arr[idx - count]
            if arr[idx] == 0 and idx - count <= last_double_idx:
                idx -= 1
                arr[idx] = 0
                count -= 1
            idx -= 1