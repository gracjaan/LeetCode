def maxVowels(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        vowels = "aeiouAEIOU"
        vowelsnum = 0
        for i in range(k):
            if s[i] in vowels: vowelsnum += 1
        result = vowelsnum
        
        for i in range(1, len(s) - k + 1):
            if s[i + k - 1] in vowels: 
                vowelsnum += 1
            if s[i-1] in vowels: 
                vowelsnum -= 1
            result = max(result, vowelsnum)
        return result
            
            
print(maxVowels("aeiou", 2))