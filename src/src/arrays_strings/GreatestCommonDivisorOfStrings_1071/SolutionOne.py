# def gcdOfStrings(str1, str2):
#     """
#     :type str1: str
#     :type str2: str
#     :rtype: str
#     """
#     i = 1
#     gcd=""
#     while (len(str1) > i or len(str2) > i):
#         if (str1[:i] == str2[:i] and str1[-i:] == str2[-i:] and str1[:i] == str1[-i:] and str2[:i] == str2[-i:] and len(str1[i:]) > len(gcd)):
#             print(str1[:i], str2[:i], str1[-i:], str2[-i:])
#             gcd = str1[:i]
#         i+=1
#     return gcd
        

# print(gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))

def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    len1 = len(str1)
    len2 = len(str2)
    minLenght = min(len1, len2)
    
    for i in range (minLenght, 0, -1):
        if (len1 % i == 0 and len2 % i == 0 and str1[:i] * (len1 // i) == str1 and str1[:i] * (len2 // i) == str2):
            return str1[:i]
    return ""
            
print(gcdOfStrings("LEET", "CODE"))