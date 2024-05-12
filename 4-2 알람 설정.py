weekdays = "주중"
weekend = "주말"
time = 0

day = int(input(weekdays + "=0," + weekend + "=1: "))

if day == 0:
    time = 7
else:
    time = 10
print("아침 10시입니다! 주인님 일어나세요!")
