"""
데이터 타입

"""

abc = [1, 2, 3, 4, 5]
print(type(abc), abc)  # <class 'list'> [1, 2, 3, 4, 5]


"""
len(x)
"""

# 일년 지출
spending_year = [25, 36, 8, 53, 24, 56, 38, 79, 94, 20, 42, 25]
print(
    type(spending_year), spending_year, len(spending_year), "개"
)  # <class 'list'> [25, 36, 8, 53, 24, 56, 38, 79, 94, 20, 42, 25] 12 개

# 상반기 지출
spending_6mon = [25, 36, 8, 53, 24, 56]
print(
    type(spending_6mon), spending_6mon, len(spending_6mon), "개"
)  # <class 'list'> [25, 36, 8, 53, 24, 56] 6 개

# 좋아하는 음식
food = ["피자", "치킨", "떡볶이", "스테이크", "딸기", "파스타"]
print("좋아하는 음식 개수:", len(food))  # 좋아하는 음식 개수: 6
print(
    "좋아하는 음식 순서:", food
)  # 좋아하는 음식 순서: ['피자', '치킨', '떡볶이', '스테이크', '딸기', '파스타']


"""
index
"""
spending = [25, 36, 8, 53, 24, 56]
print(spending[0])  # 25
spending[2] += 10
print(spending)  # [25, 36, 18, 53, 24, 56]


"""
반복문
"""
spending = [25, 36, 8, 53, 24, 56]
for s in spending:
    print(s)

for i in range(len(spending)):
    print(i + 1, "월 지출은", spending[i])

food = ["피자", "치킨", "떡볶이", "스테이크", "파스타"]
# 가장 좋아하는 음식은?
print(food[0])  # 피자
# 세 번째로 좋아하는 음식은?
print(food[2])  # 떡볶이
# 가장 덜 좋아하는 음식은?
print(food[len(food) - 1])  # 파스타
print(food[-1])  # 파스타


"""
.append(x)
"""

food = ["피자", "치킨", "떡볶이", "스테이크", "파스타"]
food.append("갑자칩")
print(food)  # ['피자', '치킨', '떡볶이', '스테이크', '파스타', '갑자칩']


"""
.remove(x)
"""

food = ["피자", "치킨", "떡볶이", "스테이크", "파스타"]
food.remove("떡볶이")
print(food)  # ['피자', '치킨', '스테이크', '파스타']


"""
del
"""

food = ["피자", "치킨", "떡볶이", "스테이크", "파스타"]
del food[-1]
print(food)  # ['피자', '치킨', '떡볶이', '스테이크']


"""
슬라이싱
"""
food = ["피자", "치킨", "떡볶이", "스테이크", "파스타"]
print(food[2:4])  # ['떡볶이', '스테이크']
print(food[:3])  # ['피자', '치킨', '떡볶이']
print(food[-2:])  # ['스테이크', '파스타']

a = "나는야 우주최강"
print(a[:3])  # 나는야
print(a[-4:])  # 우주최강


"""
.split([x])
"""
a = "나는야 우주최강"
print(a.split())  # ['나는야', '우주최강']
print(a.split()[0])  # 나는야
print(a.split()[1])  # 우주최강

date = "2021-04-15"
print(date.split("-"))  # ['2021', '04', '15']
print(date.split("-")[0])  # 2021
print(date.split("-")[1])  # 04
print(date.split("-")[2])  # 15


"""
.sort([x])
"""
food = ["피자", "치킨", "스테이크", "된장찌개", "바나나", "파스타", "감자칩"]
food.sort()
print(food)  # ['감자칩', '된장찌개', '바나나', '스테이크', '치킨', '파스타', '피자']
food.sort(reverse=True)
print(food)  # ['피자', '파스타', '치킨', '스테이크', '바나나', '된장찌개', '감자칩']

# 상반기 지출 중 가장 큰 금액 2개
spending_6mon = [25, 36, 8, 53, 24, 56]
spending_6mon.sort(reverse=True)
print(spending_6mon[:2])  # [56, 53]

# 상반기 지출 중 가장 작은 금액 2개
spending_6mon = [25, 36, 8, 53, 24, 56]
spending_6mon.sort(reverse=True)
print(spending_6mon[-2:])  # [24, 8]


"""
max(x), min(x), sum(x)
"""
spending_6mon = [25, 36, 8, 53, 24, 56]
print(max(spending_6mon), min(spending_6mon), sum(spending_6mon))  # 56 8 202


"""
.index(x)
"""

food = ["피자", "치킨", "스테이크", "된장찌개"]
search = input("찾는 음식은?")
if search in food:
    print(food.index(search) + 1, "위입니다.")
else:
    print(search, "은/는 순위에 없습니다.")


"""
이차원 리스트
"""

abc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(abc[0])  # [1, 2, 3]
print(abc[1])  # [4, 5, 6]
print(abc[2])  # [7, 8, 9]
print(abc[0][1])  # 2
print(abc[1][2])  # 6

for row in abc:
    print(row)
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]
