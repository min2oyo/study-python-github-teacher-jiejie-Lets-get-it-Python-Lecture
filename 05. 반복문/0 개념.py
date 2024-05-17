"""
라이브러리
"""

import random

print(random.random())
print(random.randrange(2, 10, 2))  # 2~9 사이의 정수(2 단위 간격)
print(random.randint(1, 10))  # 1~10 사이의 정수


"""
in	// 문자열에서만 사용 가능
"""
if "어머니" not in "아버지가방에들어가신다":
    print("yes")
else:
    print("no")


"""
break
"""
answer = int(input("숫자 입력: "))
for i in range(20):
    print(i, end=" ")
    if i == answer:
        break
