print("시작")

i = 1
num = 0

while 1:
    if "3" in str(i) or "6" in str(i) or "9" in str(i):
        num = 0
    else:
        num = i

    if int(input("입력: ")) != num:
        print("땡! 틀렸삼 정답은:", "짝")
        break

    i += 1
