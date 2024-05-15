import random

"""
1. 도서
"""
bookName = ["역사탐험대", "파이썬", "학습법", "영단어", "여행에세이", "삼국지"]
bookPrice = []

for b in bookName:
    bookPrice.append(random.randint(15000, 25000))

print(bookPrice)
max = bookPrice.index(max(bookPrice))
print(max)
print("가장 비싼 도서:", bookName[max])


"""
2. 오디션 프로그램
"""
ranking = [
    # 순위, 참가자, 이번 주 득표수, 지난주 득표수
    [1, "라이언", 956412, 564553],
    [2, "니니즈", 861832, 927175],
    [3, "어피치", 796354, 593175],
    [4, "프로도", 534840, 864326],
    [5, "네오", 387896, 648367],
]

# 1
for row in ranking:
    print(row[:2])

# 2
for row in ranking:
    if 500000 < row[2]:
        print(row[1:3])

# 3
for row in ranking:
    if row[2] < row[3]:
        print(row[1], row[2] - row[3])

# 4
for row in ranking:
    if 800000 < row[2] or 800000 < row[3]:
        print(row[1])
