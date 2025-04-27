class Solutions:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]




# test cases
solution = Solutions()
print("Test 1 - Expected [0, 1]:", solution.twoSum([2, 7, 11, 15], 9))
print("Test 2 - Expected [1, 2]:", solution.twoSum([3, 2, 4], 6))
print("Test 3 - Expected [0, 1]:", solution.twoSum([3, 3], 6))
