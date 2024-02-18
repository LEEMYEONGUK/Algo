import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
A.sort()

M = int(input())

B = list(map(int, input().split()))

for b in B:
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2

        if b > A[mid]:
            left = mid + 1

        elif b < A[mid]:
            right = mid -1

        else:
            print(1)
            break
    else:
        print(0)
        