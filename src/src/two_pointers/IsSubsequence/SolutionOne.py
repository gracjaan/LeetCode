def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        if len(s) > len(t):
            t, s = s, t
        
        slow = 0
        
        for fast in range(len(t)):
            if t[fast] == s[slow]:
                slow += 1
                if slow == len(s):
                    return True
        
        return False
        
print(isSubsequence("abc", ""))