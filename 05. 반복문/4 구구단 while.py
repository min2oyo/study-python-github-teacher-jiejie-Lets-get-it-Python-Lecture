# 교재 코드

import random

print("구구단을 외자! 구구단을 외자!")
answer, a, b = 0, 0, 0
while a * b == answer:
    a, b = random.randint(2, 9), random.randint(1, 9)
    answer = input(str(a) + " X " + str(b) + " = ")
    answer = int(answer)
print("땡! 정답은,", a * b)
