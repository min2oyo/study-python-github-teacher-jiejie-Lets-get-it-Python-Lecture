startNum = 1
lastNum = 100

print("3!69 3!69, 3!69 369~~")

for i in range(startNum, lastNum + 1):
    if "3" in str(i) or "6" in str(i) or "9" in str(i):
        print("짝", end=" ")
    else:
        print(i, end=" ")
