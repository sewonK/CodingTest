zero = [0] * 41
one = [0] * 41

def dp():
    zero[0] = one[1] = 1
    for i in range(2, 41):
        zero[i] = zero[i - 2] + zero[i - 1]
        one[i] = one[i - 2] + one[i-1]

def solution():
    dp()
    T = int(input())
    for t in range(T):
        N = int(input())
        print(zero[N], one[N])

solution()
