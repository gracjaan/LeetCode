def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fullProduct = 1
        result = []
        zeroCount = nums.count(0)
        
        for num in nums:
            if num != 0:
                fullProduct = fullProduct * num
        
        if zeroCount == 0:
            for num in nums:
                result.append(fullProduct // num)
        elif zeroCount == 1:
            for num in nums:
                if num == 0:
                    result.append(fullProduct)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(0)
            
        
        return result
    
print(productExceptSelf([-1,1,0,-3,3]))
            