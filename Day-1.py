class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 1]
    result = s.getConcatenation(nums)
    print(result)
