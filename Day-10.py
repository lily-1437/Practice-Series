def finalPrices(prices):
    n = len(prices)
    answer = [0] * n
    for i in range (n):
        answer[i] = prices[i]
        for j in range (i+1,n): 
            if (j>i and prices[j]<=prices[i]):
                answer[i] = prices[i] - prices[j]
                break
    return answer 


prices = [8,4,6,2,3]
output = finalPrices(prices)
print(output)

# def finalPrices(prices):
#     n = len(prices)
#     answer = prices[:]          # copy original prices
#     stack = []                  # stores indices

#     for i in range(n):
#         while stack and prices[i] <= prices[stack[-1]]:
#             idx = stack.pop()
#             answer[idx] -= prices[i]

#         stack.append(i)

#     return answer
