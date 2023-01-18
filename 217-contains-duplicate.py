# one-liner
# 40.99% time
# 26.52% memory

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
 
# dictionary
# 42.67% time
# 26.52% memory
 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d:
                return True
            d[n] = True
        return False
