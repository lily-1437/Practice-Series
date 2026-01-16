# this only works for single duplicate and missing numbers ╯︿╰
def findErrorNums(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2 # s= n*(n+1)//2
    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6 #Sq=n(n+1)(2n+1)//6

    actual_sum = sum(nums)
    actual_sq_sum = sum(x * x for x in nums)

    difference = actual_sum - expected_sum   # x - y
    sum_of_xplusy = (actual_sq_sum - expected_sq_sum) // difference

    duplicate = (difference + sum_of_xplusy) // 2
    missing = duplicate - difference # y = x-x+y

    return [duplicate, missing]

   
nums = [1, 2, 2, 4]

result = findErrorNums(nums)
print("Duplicate and Missing:", result)
