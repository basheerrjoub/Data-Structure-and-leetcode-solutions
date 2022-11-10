
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    length = 0
    biggestLength = 0
    sub = ""
    lengthOfS = len(s)
    i=0
    for  i in range(lengthOfS):
        char = s[i]
        if char not in sub:
            sub += char
            length = len(sub)
            if length > biggestLength:
                biggestLength = length
            
        else: #char in sub
            while char in sub:
                sub = sub[1:]
            sub += char
        
    return biggestLength

str = "dvdf"
print (lengthOfLongestSubstring(str))       
        
        