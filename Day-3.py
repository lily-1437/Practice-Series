def findMaxConsecutiveOnes(nums):
    current = 0
    maximum = 0

    for num in nums:
        if num == 1:
            current += 1
            maximum = max(maximum, current)
        else:
            current = 0

    return maximum


# ---- test run ----
nums = [1, 1, 0, 1, 1, 1]
result = findMaxConsecutiveOnes(nums)
print("Maximum consecutive 1s:", result)
