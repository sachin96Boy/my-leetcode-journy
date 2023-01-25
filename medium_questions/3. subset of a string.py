
def lengthOfLongestSubstring(s):
    
    sub = {}
    curr_sub_start = 0
    curr_len=0
    longest=0

    for i, letter in enumerate(s):

        if letter in sub and sub[letter] >= curr_sub_start:
            curr_sub_start = sub[letter] + 1
            curr_len = i - sub[letter]
            sub[letter] = i

        else:
            sub[letter] = i
            curr_len += 1
            if curr_len > longest:
                longest = curr_len

    return longest
        
s = "aab"
res = lengthOfLongestSubstring(s)

print(res)