def compress(chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.sort()
        result = [] 
        reps = 1
        
        for i in range (0, len(chars)):
            if i == len(chars) - 1:
                if reps == 1:
                    result.append(chars[i])
                else:
                    result.append(chars[i])
                    result.append(str(reps))
            elif chars[i+1] == chars[i]:
                reps += 1
            else:
                if reps == 1:
                    result.append(chars[i])
                else:
                    result.append(chars[i])
                    result.append(str(reps))
                reps = 1
        return result
            
print(compress(["a","a","b","b","c","c","c"]))
                
            
        