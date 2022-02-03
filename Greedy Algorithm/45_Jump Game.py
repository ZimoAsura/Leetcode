class Solution:
    def jump(self, nums: List[int]) -> int:
        # 贪心算法的思路
        # 用三个变量start,end,maxpos分别表示跳跃的起始位置，终点位置以及跳跃过程中发现的下一次跳跃的最远位置
        # 初始化是start = end = 0，因为一开始的时候还没有跳
        n = len(nums)
        start = 0
        end = 0
        maxpos = 0
        count = 0
        for i in range(n-1):
            maxpos = max(maxpos, i + nums[i])
            if i == end:#跳到了这个位置
                start = end+1
                end = maxpos
                count += 1 #更新步长
        return count