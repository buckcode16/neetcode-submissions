class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            if operations[i] == "+":
                val =  int(stack[-1]) + int(stack[-2])
                stack.append(val)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                val = int(stack[-1])*2
                stack.append(val)
            else:
                stack.append(int(operations[i]))


        return sum(stack)