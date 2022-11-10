// https://leetcode.com/problems/goal-parser-interpretation

class Solution(object):
    def interpret(self, command):
        newCommand = ""
        i = 0
        while i in range(len(command)):
            if command[i] == "(":
                if command[i+1] == "a":
                    newCommand += "al"
                    i += 4
                elif command[i+1] == ")":
                    newCommand += "o"
                    i += 2
            else:
                newCommand += command[i]
                i += 1
        return newCommand
            

