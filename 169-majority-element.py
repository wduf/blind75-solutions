# 99.49% time
# 30.58% space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur, cnt = nums[0], 1
        for n in nums:
            cnt += 1 if n == cur else -1
            if not cnt:
                cur, cnt = n, 1
        return cur
