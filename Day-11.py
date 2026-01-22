def dailyTemperatures(temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                  indx = stack.pop()
                  answer[indx] = i - indx
            stack.append(i)
        return answer
        

temperatures = [73,74,75,71,69,72,76,73]
output = dailyTemperatures(temperatures)
print(output)