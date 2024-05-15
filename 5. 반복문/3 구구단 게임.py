import random

count = 10
dan = 0
num = 0
answer = 0
score = 0

for i in range(count):
    print("\ncount:", i + 1, "/", count)
    dan = random.randint(2, 9)
    num = random.randint(1, 9)
    question = str(dan) + " X " + str(num) + " = "
    answer = int(input(question))
    if dan * num == answer:
        print("딩동댕")
        score += 1
    else:
        print("땡, 5번 반복해 읽으세요")
        for j in range(5):
            print(question, dan * num)
    print("count:", score)

print("끝!")
