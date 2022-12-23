class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
        # return sum of the range of numbers + 1 
        # so len [3,0,1] + 1 == 4
        # range(4) == 0,1,2,3
        # sum(range(4)) == 0 + 1 + 2 + 3 = 6
        # 6 - sum([3,0,1]) == 2
