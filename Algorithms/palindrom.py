
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    sub = ""
    longest = ""
    for i in range(len(s)):
        
        leftI = i-1
        rightI = i+1
        while leftI+1 >=0 and rightI < len(s) and s[leftI+1] == s[rightI]:
            sub = s[leftI+1:rightI+1]
            if len(sub) > len(longest):
                longest = sub
            rightI +=1 
            leftI -=1
        leftI = i-1
        rightI = i+1
        while leftI >=0 and rightI < len(s) and s[leftI] == s[rightI]:
            sub = s[leftI:rightI+1]
            if len(sub) > len(longest):
                longest = sub
            leftI -=1
            rightI +=1
        

    return longest
print (longestPalindrome("jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"))
    