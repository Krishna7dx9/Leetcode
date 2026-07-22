class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        max_area = 0
        stack = []

        for idx in range(len(heights)):
            
            while stack and heights[stack[-1]] > heights[idx]:      # current deight smaller
                popped = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1

                height = heights[popped]
                width = idx - left - 1
                area = height * width
                max_area = max(max_area, area)

            stack.append(idx)

        return max_area