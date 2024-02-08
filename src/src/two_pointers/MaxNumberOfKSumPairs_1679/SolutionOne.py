def maxOperations(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        result = 0
        nums.sort()
        
        while left < right:
            if nums[left] + nums[right] == k:
                result += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return result