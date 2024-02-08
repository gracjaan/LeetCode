def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        places=0
        
        if (len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1) or n == 0:
            return True
        elif len(flowerbed) == 1 and (flowerbed[0] == 1 or n > 1):
            return False
        
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    places += 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    places += 1
                    flowerbed[i] = 1
            elif (flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
                places += 1
                flowerbed[i] = 1
                
        return places >= n
    
canPlaceFlowers([1,0,0,0,1],2)