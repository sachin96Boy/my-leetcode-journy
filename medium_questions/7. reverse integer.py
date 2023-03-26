# Input:  num
# (1) Initialize sign value, based on the sighn is (-) take he abosolute value in value
# (2) Loop while num > 0
#      (a) Multiply rev_num by 10 and add remainder of num  
#           divide by 10 to rev_num
#                rev_num = rev_num*10 + num%10;
#      (b) Divide num by 10
# (3) Return rev_num

class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        rev = 0
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        if rev > 2**31 - 1 or rev < -2**31:
            return 0
        else:
            return sign * rev