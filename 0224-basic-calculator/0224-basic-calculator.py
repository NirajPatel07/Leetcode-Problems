class Solution:
    def calculate(self, s: str) -> int:
        currNum = None
        stack = []
        
        result = None
        
        ops = { '+': lambda x, y: x + y, '-': lambda x, y: x - y }
        
        i = 0
        while i < len(s):
            # print(stack)
            if s[i] in "+":
                stack.append(s[i])
            elif s[i] == '-':
                if not stack or stack[-1] == '(':
                    stack.append(0)
                stack.append(s[i])
            elif s[i] == '(':
                stack.append('(')
            elif s[i] == ' ':
                None
            else:
                if s[i].isdigit():
                    currNum = int(s[i])
                    i+=1
                    while i < len(s) and s[i].isdigit():
                        currNum *= 10
                        currNum += int(s[i])
                        i+=1
                    i -= 1
                elif s[i] == ')':
                    currNum = stack.pop()
                    stack.pop()
                if stack and stack[-1] in '+-':
                    stack.append(ops[stack.pop()](stack.pop(), currNum))
                else:
                    stack.append(currNum)
            i+=1
        return stack.pop()