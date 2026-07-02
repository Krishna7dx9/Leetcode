class Solution(object):
    def maxSlidingWindow(self, nums, k):
        max_array = []

        for left in range(len(nums) - k + 1):
            right = left + k
            window = nums[left: right]
            max_array.append(max(window))

        return max_array
  