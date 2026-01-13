class Solution(object):
    def shuffle(self, nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])      # xi
            ans.append(nums[i + n])  # yi

        return ans


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(s.shuffle(nums, n))  # Expected: [2, 3, 5, 4, 1, 7]

    # Test case 2
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(s.shuffle(nums, n))  # Expected: [1, 4, 2, 3, 3, 2, 4, 1]

    # Test case 3
    nums = [1, 1, 2, 2]
    n = 2
    print(s.shuffle(nums, n))  # Expected: [1, 2, 1, 2]
