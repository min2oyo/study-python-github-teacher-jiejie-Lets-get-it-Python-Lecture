priceEvent = 100000

price = int(input("금액: "))
isReceiveMarketing = input("마케팅 이용약관 동의 Y/N: ")

if price >= priceEvent and isReceiveMarketing == "Y":
    print("사은품 지급 대상입니다.")
else:
    print("사은품 지급 대상이 아닙니다.")
