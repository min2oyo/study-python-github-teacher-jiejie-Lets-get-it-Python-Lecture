priceOfAdult = 15000
priceOfChild = 6000
price = 0
priceOfInput = 0
age = int(input("나이: "))

if age >= 20:
    print("성인은", priceOfAdult, "원입니다.")
    price = priceOfAdult
else:
    print("미성년자는", priceOfChild, "원입니다.")
    price = priceOfChild

priceOfInput = int(input("투입금액: "))

if priceOfInput < price:
    print(price - priceOfInput, "원을 더 넣어주세요.")
elif priceOfInput >= price:
    if priceOfInput > price:
        print("거스름돈 ", priceOfInput - price, "입니다.")
    print("감사합니다. 즐거운 시간 되세요!")
