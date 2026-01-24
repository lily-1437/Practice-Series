def largestRectangleArea(height):
    n = len(height)
    answer = 0
    stack = []

    for i in range(n):
        while stack and height[i] < height[stack[-1]]:
            length = height[stack.pop()]
            right = i
            left = stack[-1] if stack else -1
            width = right - left - 1
            answer = max(answer, length * width)
        stack.append(i)

    # process remaining bars at 6
    while stack:
        length = height[stack.pop()]
        right = n
        left = stack[-1] if stack else -1
        width = right - left - 1
        answer = max(answer, length * width)

    return answer

height = [2,1,5,6,2,3]
output = largestRectangleArea(height)
print(output)