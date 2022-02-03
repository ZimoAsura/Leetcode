class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心思路,不断的计算在每一格能跳到最远的距离
        # 如果最远距离<= i了说明它无法到达后面的格子
        n = len(nums)
        farther = 0
        for i in range(n - 1):
            farther = max(farther, i + nums[i])
            if farther < i + 1:
                return False
        return farther >= n - 1

