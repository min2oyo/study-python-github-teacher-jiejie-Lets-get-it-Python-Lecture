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
    answer = int(input(str(dan) + " X " + str(num) + " = "))
    if dan * num == answer:
        print("딩동댕")
        score += 10
    else:
        print("땡")
    print("count:", score)

print("끝!")
