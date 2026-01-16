def smallerNumbersThanCurrent(nums):
    # Step 1: Frequency array (0–100 is safe for this problem)
    freq = [0] * 101
    
    for num in nums:
        freq[num] += 1 # how many time the numbers from the array appear

    # Step 2: Prefix sum
    for i in range(1, 101):
        freq[i] += freq[i - 1] # how many numbers are less than i

    # Step 3: Build result
    result = []
    for num in nums:
        if num == 0:
            result.append(0)
        else:
            result.append(freq[num - 1])

    return result

nums = [8,1,2,2,3]
output = smallerNumbersThanCurrent(nums)
print(output)