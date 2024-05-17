import operator

"""
1. 요일
"""
day = {
    "월요일": "Mon",
    "화요일": "Tue",
    "수요일": "Wed",
    "목요일": "Thu",
    "금요일": "Fri",
}

# 1
day["토요일"] = "Sat"
day["일요일"] = "Sun"
print(
    day
)  # {'월요일': 'Mon', '화요일': 'Tue', '수요일': 'Wed', '목요일': 'Thu', '금요일': 'Fri', '토요일': 'Sat', '일요일': 'Sun'}

# 2
day["일요일"] = "SUN"
print(
    day
)  # {'월요일': 'Mon', '화요일': 'Tue', '수요일': 'Wed', '목요일': 'Thu', '금요일': 'Fri', '토요일': 'Sat', '일요일': 'SUN'}

# 3
del day["수요일"]
print(
    day
)  # {'월요일': 'Mon', '화요일': 'Tue', '목요일': 'Thu', '금요일': 'Fri', '토요일': 'Sat', '일요일': 'SUN'}


"""
2. 서점
"""
book = {
    "역사대모험": 20000,
    "영단어": 9000,
    "파이썬": 17000,
    "여행에세이": 22000,
    "삼국지": 33000,
}

for b in book:
    if book[b] <= 15000:
        book[b] += 1.1
    else:
        book[b] += 1.05
print(book)
# {'역사대모험': 21000.0, '영단어': 9900.0, '파이썬': 17850.0, '여행에세이': 23100.0, '삼국지': 34650.0}


"""
3. 오디션
"""
ranking = {
    "라이언": 956412,
    "어피치": 796354,
    "니니즈": 861832,
    "네오": 387896,
    "프로도": 534840,
}
ranking_result = sorted(ranking.items(), key=operator.itemgetter(1), reverse=True)
print(ranking_result)
for k, v in ranking_result:
    print(k, end=" ")
