class Solution:
    def largestRectangleArea(self, heights):

        stack = []
        maxArea = 0

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                h = heights[stack.pop()]

                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                maxArea = max(maxArea, h * w)

            stack.append(i)

        while stack:

            h = heights[stack.pop()]

            if not stack:
                w = len(heights)
            else:
                w = len(heights) - stack[-1] - 1

            maxArea = max(maxArea, h * w)

        return maxArea