def isPalindrome(s=[1,2,3,4,5,4,3,2,1]):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and isPalindrome(s[1:-1])

#After running the code type isPalindrome([1,2,3,4,5,4,3,2,1]) and hit enter.
