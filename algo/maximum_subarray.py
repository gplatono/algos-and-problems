from typing import *
import sys

# The original Kadane's algorithm.
def kadanesAlgorithm(nums: List[float]) -> float:
    current_max = 0
    best_max = sys.float_info.min
    for num in nums:
        current_max = max(num, current_max + num)
        best_max = max(best_max, current_max)
    
    return best_max

# A variation of Kadane's algorithm that uses running global min
# rather than current max.
def minMaxDiffAlgorithm(nums: List[float]) -> float:
    best_min = 0
    best_max = sys.float_info.min
    running_sum = 0
    for num in nums:
        running_sum += num
        best_max = max(best_max, running_sum, running_sum - best_min)
        best_min = min(best_min, running_sum)

    return best_max

kadanesAlgorithm([-1.0])