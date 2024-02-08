def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        i = 0
        while (len(word1) > i and len(word2) > i):
            output += word1[i] + word2[i]
            i+=1
        if (len(word1) > i):
            output += word1[i:]
        if (len(word2) > i):
            output += word2[i:]
        return output

print(mergeAlternately("ab", "pqrs"))