startNum = 1
lastNum = 30

for i in range(startNum, lastNum + 1):
    if i % 2:
        print(i, "홀수", end="")
    else:
        print(i, "짝수", end="")
    if i != lastNum:
        print(end=", ")
