from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        max_array = []

        # store indices of useful maximum candidates
        window = deque()

        for right in range(len(nums)):

            # Remove smaller elements from back
            # They can never become future maximum
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            # Add current index
            window.append(right)

            # Remove front if it left current window
            if window[0] <= right - k:
                window.popleft()

            # Window complete
            if right >= k - 1:

                # Front always stores maximum index
                max_array.append(nums[window[0]])

        return max_array