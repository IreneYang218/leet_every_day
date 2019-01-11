def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, val in enumerate(nums):
            for idx2 in range(idx+1, len(nums)):
                if (val + nums[idx2]) == target:
                    return [idx, idx2]

# test
nums = [2,7,11,15]
target = 9

twoSum(nums, target)