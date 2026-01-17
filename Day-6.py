#this only works for 1 to n range
def findDisappearedNumbers(nums):
    n = len(nums)
    for i in range (n):
        index = abs(nums[i])-1
        if(nums[index]>0):
            nums[index] = -nums[index]
    result = []
    for i in range (n):
        if (nums[i]>0):
            result.append(i+1)
    return result

nums = [4,3,2,7,8,2,3,1]
result = findDisappearedNumbers(nums)
print(result)

''' for finding duplicate numbers
def findDuplicateNumbers(nums):
    freq = [0] *(len(nums)+1)
    result = []
    for i in nums:
        freq[i] +=1
        if(freq[i]>1):
            result.append(i)
    return result

nums = [1,3,2,7,8,2,3,1]
result = findDuplicateNumbers(nums)
print(result)'''