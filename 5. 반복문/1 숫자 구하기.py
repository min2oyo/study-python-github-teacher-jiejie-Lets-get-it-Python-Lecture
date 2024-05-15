startNum = 1
lastNum = 50

"""
for - 합
"""
totalNumber = 0

for i in range(startNum, lastNum + 1):
    totalNumber += i

print(totalNumber)


"""
while - 곱
"""
i = startNum
totalNumber = 1

while i < lastNum + 1:
    totalNumber *= i
    i += 1

print(totalNumber)
