class Solution:
    def trap(self, height):
        stack = []
        volume = 0

        for i in range(len(height)):
            """
            변곡점을 만난다 (현재 높이가 이전 보다 높을 때)
            현재 : height[i]
            이전 : height[stack[-1]]
            """
            while stack and height[i] > height[stack[-1]]:

                top = stack.pop()

                # stack 이 empty 면 break -> 왼쪽에서 물을 가둬줄 벽이 없기 때문
                if not len(stack):
                    break

                # 굳이 표현하면 가로 길이
                distance = i - stack[-1] - 1

                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += (distance * waters)
            stack.append(i)
        return volume


solution = Solution()
print(solution.trap([4, 2, 0, 3, 2, 5]))
