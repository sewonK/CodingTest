# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
# phone_book = ["12","123","1235","567","88"]
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(0, len(phone_book) - 1):
        if(phone_book[i] == phone_book[i+1][0:len(phone_book[i])]):
            answer = False
            break
    return answer
# print(solution(phone_book))

# Best 풀이
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
