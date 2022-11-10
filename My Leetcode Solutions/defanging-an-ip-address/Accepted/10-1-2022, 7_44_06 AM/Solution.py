// https://leetcode.com/problems/defanging-an-ip-address

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        newString = ""
        i = 0
        while i in range(len(address)-1):
            if address[i+1] == ".":
                newString += address[i] + "[.]"
                i += 2
            else:
                newString += address[i]
                i += 1
        newString += address[i]
        return newString