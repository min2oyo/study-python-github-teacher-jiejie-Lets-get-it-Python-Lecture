import random

score = []

for i in range(25):
    score.append(random.randint(0, 100))

print(score)

# 방법 1
for s in score:
    if 70 <= s:
        print("학생번호:", score.index(s) + 1, "점수:", s)

# 방법 2
for i in range(len(score)):
    if 70 <= score[i]:
        print("학생번호:", i + 1, "점수:", score[i])


# 방법 1 주의
score = [1, 2, 1, 1, 3]

for s in score:
    print("학생번호:", score.index(s) + 1, "점수:", s)
    # 학생번호: 1 점수: 1
    # 학생번호: 2 점수: 2
    # 학생번호: 1 점수: 1
    # 학생번호: 1 점수: 1
    # 학생번호: 5 점수: 3
