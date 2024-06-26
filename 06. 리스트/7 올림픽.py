olympic = [
    [1, "미국", 46, 37, 38, 121],
    [2, "영국", 27, 23, 17, 67],
    [3, "중국", 26, 18, 26, 70],
    [4, "러시아", 19, 18, 19, 55],
    [5, "독일", 17, 10, 15, 42],
    [6, "일본", 12, 8, 21, 41],
    [7, "프랑스", 10, 18, 14, 42],
    [8, "대한민국", 9, 3, 9, 21],
]

# 미국 독일 금메달 개수
print(olympic[0][1], "금메달 개수:", olympic[0][2])  # 미국 금메달 개수: 46
print(olympic[4][1], "금메달 개수:", olympic[4][2])  # 독일 금메달 개수: 17

# 미국 독일 금은동 개수
print(
    olympic[0][1], "금은동 메달 개수:", olympic[0][2:5]
)  # 미국 금은동 메달 개수: [46, 37, 38]

print(
    olympic[4][1], "금은동 메달 개수:", olympic[4][2:5]
)  # 독일 금은동 메달 개수: [17, 10, 15]

print(olympic[:4])
# [[1, '미국', 46, 37, 38, 121], [2, '영국', 27, 23, 17, 67], [3, '중국', 26, 18, 26, 70], [4, '러시아', 19, 18, 19, 55]]

print(olympic[:4][1])
# [2, '영국', 27, 23, 17, 67]

print(olympic[1])
# [2, '영국', 27, 23, 17, 67]

# 순위와 국가명
for row in olympic:
    print(row[:2])
# [1, "미국"]
# [2, "영국"]
# [3, "중국"]
# [4, "러시아"]
# [5, "독일"]
# [6, "일본"]
# [7, "프랑스"]
# [8, "대한민국"]

# 금메달보다 은메달이 더 많은 나라
for row in olympic:
    if row[2] < row[3]:
        print(row[1])  # 프랑스

# 모든 국가가 획득한 금메달 개수의 합
totalGold = 0
for row in olympic:
    totalGold += row[2]
print(totalGold)  # 166

# 나라면 총 메달 개수 중 금메달이 차지하는 비율이 40%가 넘는 나라
for row in olympic:
    goldRate = row[2] / (row[2] + row[3] + row[4]) * 100
    if goldRate > 40:
        print(row[1], goldRate, "%")
    # 영국 40.298507462686565 %
    # 독일 40.476190476190474 %
    # 대한민국 42.857142857142854 %
