class Solution:
    def calPoints(self, operations: List[str]) -> int:

        
        stack = []

        #print(f"Before: {operations}")
        
        for x in operations:
            if x == "C":
                stack.pop()
                #print(f"C: {stack}")
            elif x == "D":
                stack.append((stack[-1]*2))
                #print(f"D: {stack}")
            elif x == '+':
                #print(f"+: {stack}")
                num = stack[-1]
                #print(f"+: {num}")
                stack.pop()
                #print(f"+: {stack}")
                num2 = stack[-1]
                #print(f"+: {num2}")
                stack.append(num)
                stack.append(num + num2)
                #print(f"+: {stack}")
            else:
                num = int(x)
                stack.append(num)
                #print(f"int: {stack}")

        sum = 0

        for x in stack:
            sum += x

        return sum

        