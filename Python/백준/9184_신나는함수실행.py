w = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
def dp():
    for a in range(21):
        for b in range(21):
            for c in range(21):
                if a <= 0 or b <= 0 or c <= 0:
                    w[a][b][c] = 1
                elif a < b and b < c:
                    w[a][b][c] = w[a][b][c-1] + w[a][b-1][c-1] - w[a][b-1][c]
                else:
                    w[a][b][c] =  w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]

def solution():
    dp()
    while(1):
        a, b, c = map(int, input().split(' '))
        if a == b == c == -1:
            break
        
        if a <= 0 or b <= 0 or c <= 0:
            print(f'w({a}, {b}, {c}) = 1')
        elif a > 20 or b > 20 or c > 20:
            print(f'w({a}, {b}, {c}) = {w[20][20][20]}')
        else:
            print(f'w({a}, {b}, {c}) = {w[a][b][c]}')

solution()