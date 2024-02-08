def largestAltitude(gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0]
        for n, num in enumerate(gain):
            altitudes.append(altitudes[n] + num)
        return max(altitudes)