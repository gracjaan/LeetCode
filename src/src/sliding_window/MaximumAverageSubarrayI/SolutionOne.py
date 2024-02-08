def findMaxAverage(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ksum = sum(nums[:k])
        result = ksum / k

        for i in range(1, len(nums) - k + 1):
            ksum = ksum - nums[i-1] + nums[i+k-1]
            result = max(result, ksum / k)
        
        return result
    
print(findMaxAverage([4,2,1,3,3], 2))