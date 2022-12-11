class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()        
        # valid triange == c < a + b
        # decrementing range from last index to but not reaching 2 by -1
        for i in range( (len(A) - 1) , 1 , -1):
            if A[i] < A[i - 1] + A[i - 2]:
                return A[i] + A[i - 1] + A[i - 2]
        return 0
        
        
