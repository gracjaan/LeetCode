def solution(A, B):
    n = len(A)
    max_val = float('inf')
    for i in range(n):
        for j in range(n):
            if A[i] <= B[j]:
                path_max = max(A[i:j+1] + B[i+1:j+1])
                max_val = min(max_val, path_max)
    return max_val

print(solution([3,4,6], [6,5,4]))