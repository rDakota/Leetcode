class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while (n != 0):
            if n % 2 == 1: # if last digit is a 1
                count += 1 # add to count
            n = n // 2 # int division to decrement the number
        return count
