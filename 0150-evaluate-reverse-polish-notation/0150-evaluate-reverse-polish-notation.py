class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #for reverse polish arithmetic expression, we always have two expressions before an operator if we want to 
        #involve the expressions in the given operator!

        #And since we can feed the result of one expression into another operation with a different operand that came before it(kinda like chaining), we need to always know the most recently seen expressions!

        #We can keep track of most recently seen expression by utilizing a stack data structure!(LIFO ORDERING)

        #Thus, what we can do is, if we come across a number, simply push to top of stack!
        #If we come across an operand, apply operation on top two elements of stack and push the result back onto
        #top of stack!


        #at the end, the only 1 element remaining in stack will be our answer!
        #we will use end of array as top of stack!
        stack = []
        #s will be set of arithmetic operations: add, minus, divide, and multiply!
        s = set()
        s.add("+")
        s.add("-")
        s.add("/")
        s.add("*")
        for e in tokens:
            #it's a number!
            if(e not in s):
                stack.append(e)
                continue
            #if it's an operator, pop top 2 elements from stack and typecast to int!
            else:
                second_operand = int(stack.pop())
                first_operand = int(stack.pop())
                if(e == "+"):
                    stack.append(str(first_operand + second_operand))
                    continue
                elif(e == "-"):
                    stack.append(str(first_operand - second_operand))
                    continue
                elif(e == "*"):
                    stack.append(str(int(first_operand * second_operand)))
                    continue
                else:
                    stack.append(str(math.trunc(first_operand / second_operand)))
        return int(stack[0])