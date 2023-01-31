# 95.39% time
# 96.59% memory

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        fi, bi = 0, len(nums) - 1  # front index, back index
        i = 0
        while i <= bi:
            match nums[i]:
                case 0:
                    nums[i], nums[fi] = nums[fi], nums[i]
                    fi += 1
                case 2:
                    nums[i], nums[bi] = nums[bi], nums[i]
                    bi -= 1
                    continue
                case _:
                    pass
            i += 1
