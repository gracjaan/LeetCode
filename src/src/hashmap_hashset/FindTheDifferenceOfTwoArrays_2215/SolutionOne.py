def findDifference(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        n1 = set(nums1)
        n2 = set(nums2)

        common_elements = n1.intersection(n2)

        n1.difference_update(common_elements)
        n2.difference_update(common_elements)

        return [list(n1), list(n2)]
    
        # Alternatively
        # return [set(nums1) - set(nums2), set(nums2) - set(nums1)]


print(findDifference([1,2,3,3], [1,1,2,2]))