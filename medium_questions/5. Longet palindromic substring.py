# To find the longest palindromic substring in a given string s,
# we can use a dynamic programming approach that leverages
# the fact that a palindrome is the same forwards and backwards.

# We can define a boolean 2D array dp[i][j]
# where dp[i][j] is true if the substring s[i:j+1] is a palindrome and false
# otherwise. We start by initializing all dp[i][i] to true 
# since a single character is always a palindrome. 
# Then, we iterate over all substring lengths l from 2 to the length of s.
# For each length l, we iterate over 
# all starting indices i from 0 to the length of s minus l.
# We calculate the ending index j as i + l - 1 and set dp[i][j] to true 
# if s[i] is equal to s[j] and the substring s[i+1:j] is also a palindrome 
# (i.e., dp[i+1][j-1] is true). 

# If dp[i][j] is true and the length of the palindrome is greater 
# than the current longest palindrome, 
# we update the longest palindrome.

def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    longest_palindrome = ""

    # all substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
        longest_palindrome = s[i]

    # check substrings of length 2 or greater
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if s[i] == s[j]:
                if l == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if len(longest_palindrome) < l:
                        longest_palindrome = s[i:j+1]

    return longest_palindrome
