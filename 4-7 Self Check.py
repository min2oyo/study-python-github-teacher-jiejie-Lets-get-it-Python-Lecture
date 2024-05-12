"""
1. 독감
"""

normalTemperature = 38.5

isCouch = input("기침을 하나요? Y/N:")
temperature = float(input("체온: "))

if isCouch == "Y" and temperature >= normalTemperature:
    print("독감일 수 있습니다.")


"""
2. 분식집
"""

vegetableGim = 2500
tunaGim = 3500
ramen = 3500
koreaRiceRamen = 4000
dumplingRamen = 4000

menu = int(input("김밥=1, 라면=2:"))

if 1 == menu:
    print("vegetableGim:", vegetableGim)
    print("tunaGim:", tunaGim)
elif 2 == menu:
    print("ramen", ramen)
    print("koreaRiceRamen", koreaRiceRamen)
    print("dumplingRamen", dumplingRamen)
else:
    print("올바른 메뉴를 입력해 주세요.")


"""
3. 점수
"""

score = int(input("점수: "))

if 0 < score < 100:
    if 80 < score:
        print("A등급")
    elif 40 < score:
        print("B등급")
    else:
        print("C등급")
else:
    print("잘못된 숫자를 입력했습니다.")
