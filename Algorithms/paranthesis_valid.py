def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        par1 = "[]"
        par2 = "()"
        par3 = "{}"
        while len(s) > 0:
            if par1 in s:
                s.replace(par1, "")
            elif par2 in s:
              s =   s.replace(par2, "")
            elif par3 in s:
                s.replace(par3, "")
            else:
                return False
        return True

print(isValid("()"))