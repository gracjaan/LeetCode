def increasingTriplet (nums):
    first = float('inf')
    second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False


print(increasingTriplet([5,1,5,5,0,8]))