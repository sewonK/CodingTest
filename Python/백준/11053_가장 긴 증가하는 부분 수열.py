def binary_search(LIS, target):
    start = 0
    end = len(LIS) - 1
    while(start <= end):
        mid = (start + end) // 2
        if LIS[mid] == target:
            return mid
        elif LIS[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


def solution():
    N = int(input())
    A = list(map(int, input().split(' ')))
    LIS = [A[0]]
    for i in range(1, N):
        if A[i] > LIS[len(LIS) - 1]:
            LIS.append(A[i])
        else:
            idx = binary_search(LIS, A[i])
            LIS[idx] = A[i]    

    return len(LIS)

print(solution())