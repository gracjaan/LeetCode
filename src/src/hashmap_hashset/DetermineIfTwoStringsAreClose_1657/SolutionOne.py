def closeStrings(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    l1 = list(word1)
    dict1 = {}
    l2 = list(word2)
    dict2 = {}

    for n in l1:
        if n in dict1:
            dict1[n] += 1
        else:
            dict1[n] = 1
    
    for n in l2:
        if n in dict2:
            dict2[n] += 1
        else:
            dict2[n] = 1
    
    o1 = []
    o2 = []
    for k in dict1:
        o1.append(dict1[k])
    for k in dict2:
        o2.append(dict2[k])
    
    so1 = sorted(o1)
    so2 = sorted(o2)
    
    print(so1, so2)
    
    return so1 == so2

print(closeStrings("uau", "ssx"))