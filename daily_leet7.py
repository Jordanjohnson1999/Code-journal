class Solution:
    def findMax(self, nums):
        max_num = nums[0]
        for num in nums:
            if num > max_num:
                max_num = num
        return max_num

        pass

solution = Solution()


# test cases
print("Test 1 - Expected: 8 | Got:", solution.findMax([2,5,1,8,4]))
print("Test 2 - Expected: 30 | Got:", solution.findMax([10,20,30,5,15]))
print("Test 3 - Expected: 5 | Got:", solution.findMax([5]))
