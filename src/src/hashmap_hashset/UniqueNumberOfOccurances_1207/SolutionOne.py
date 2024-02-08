def uniqueOccurrences(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        for n in arr:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
        
        occurances = []
        for k in dict:
            occurances.append(dict[k])
        
        return len(occurances) == len(set(occurances))