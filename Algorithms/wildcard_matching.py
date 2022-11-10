def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    # case of asterisk
    if p.find("*") != -1:
        i = 0
        j = 0
        while i < len(s):
            if p[j] == "*" and (j + 1) != len(p):
                i += 1
                continue
            elif p[j] == "?":
                pass
            elif s[i] != p[j]:
                return False

            i += 1
            j += 1
        return True


print(isMatch("1233mkadca", "124*ca"))
