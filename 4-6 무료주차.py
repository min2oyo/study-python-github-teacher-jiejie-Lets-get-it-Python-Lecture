priceFree = 100000

price = int(input("금액: "))
isReceiveMarketing = input("마케팅 이용약관 동의 Y/N: ")

if price >= priceFree or isReceiveMarketing == "Y":
    print("무료주차 대상입니다.")
else:
    print("무료주차 대상이 아닙니다.")
