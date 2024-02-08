def kidsWithCandies( candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        maxCandies = max(candies)
        
        for child in candies:
            b = child + extraCandies >= maxCandies
            result.append(b)
        return result
        
print(kidsWithCandies([2,3,5,1,3], 3))