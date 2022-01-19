def distance(a, b):
    a -= 1
    b -= 1
    ax = a // 3
    ay = a % 3
    bx = b // 3
    by = b % 3
    return abs(ax - bx) + abs(ay - by)

def moveL(number):
    global answer, left
    answer += 'L'
    left = number

def moveR(number):
    global answer, right
    answer += 'R'
    right = number

def solution(numbers, hand):
    global answer, left, right
    answer = ''
    left = 10
    right = 12
    for number in numbers:
        if number in (1, 4, 7):
            moveL(number)
        elif number in (3, 6, 9):
            moveR(number)
        else:
            if number == 0:
                number = 11
            leftD = distance(left, number)
            rightD = distance(right, number)
            if leftD > rightD:
                moveR(number)
            elif rightD > leftD:
                moveL(number)
            else:
                if hand == 'right':
                    moveR(number)
                else:
                    moveL(number)
    return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))