class Solution:
    def maximum69Number (self, num: int) -> int:
        # Return the maximum number you can get by changing at most one digit
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == '9':
                continue
            else:
                num[i] = '9'
                break
        return int("".join(num))