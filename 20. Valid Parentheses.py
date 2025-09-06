class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        if len(s) == 0 or len(s) == 1:
            return False

        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False

        for x in s:
            if x == "(":
                stack.append(x)
                #print(stack)
            elif x == "{":
                stack.append(x)
                #print(stack)
            elif x == "[":
                stack.append(x)
                #print(stack)
            elif x == ")":
                if not stack:
                    return False
                elif "(" == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif x == "}":
                if not stack:
                    return False
                elif "{" == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif x == "]":
                if not stack:
                    return False
                elif "[" == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        #print(stack)
        if not stack:
            return True
        else:
            return False