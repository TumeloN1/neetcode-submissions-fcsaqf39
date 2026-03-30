class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       '''
       idea: maintain 2 stacks
       main stack contains all values in the list with first item at the top
       second stack will contain operands
       pop operands from the main stack until we reach an operator
       when we reach an operator, pop 2 values from the operand stack and push
       the result
       continue until the main stack is empty and then output the value that
       remains in the operand stack
       '''
       operands = []
       expression = tokens[::-1]
       while len(expression) > 0:
            token = expression.pop()
            if not token in ["+","-","*","/"]:
                operands.append(int(token))
            else:
                t1 = operands.pop()
                t2 = operands.pop()
                if token == "*":
                    res = t2 * t1
                elif token == "+":
                    res = t2 + t1
                elif token == "-":
                    res = t2 - t1
                elif token == "/":
                    res = int(t2 / t1)
                operands.append(res)
       return operands.pop()