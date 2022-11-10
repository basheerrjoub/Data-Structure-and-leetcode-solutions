// https://leetcode.com/problems/truncate-sentence

class Solution(object):
    def truncateSentence(self, s, k):
        
        count = 0
        i = 0
        while i < len(s):
            if s[i] == " ":
                count += 1 
                if count == k:
                    return s[:i]
            
            i+=1
        return s