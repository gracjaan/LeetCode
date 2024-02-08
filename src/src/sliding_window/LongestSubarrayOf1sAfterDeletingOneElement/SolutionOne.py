def longestSubarray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        nzero = 0
        if nums[0] == 0 : nzero = 1
        longest = 0
        
        while right < len(nums) - 1:
            if nzero > 1 and left < right:
                left += 1
                if nums[left - 1] == 0: 
                    nzero -= 1
            else:
                longest = max(longest, right - left)
                right += 1
                if nums[right] == 0: 
                    nzero += 1
        
        longest = max(longest, right - left)
        return longest
    
print(longestSubarray([0,0,0]))