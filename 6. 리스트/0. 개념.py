"""
데이터 타입

"""

abc = [1, 2, 3, 4, 5]
print(type(abc), abc)  # <class 'list'> [1, 2, 3, 4, 5]


"""
len()
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
