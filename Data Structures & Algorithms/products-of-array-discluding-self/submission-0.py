class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        # Step 1: Create arrays
        left = [1] * n
        right = [1] * n
        answer = [1] * n

        # Step 2: Fill the left array
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Step 3: Fill the right array
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Step 4: Multiply left and right
        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer