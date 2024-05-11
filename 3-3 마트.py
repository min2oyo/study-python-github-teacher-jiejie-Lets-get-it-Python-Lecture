snack = 1200
ramen = 800
ham = 2400

countOfSnack = int(input("과자: "))  # 3
countOfRamen = int(input("라면: "))  # 5
countOfHam = int(input("햄: "))  # 2

totalPrice = snack * countOfSnack + ramen * countOfRamen + ham * countOfHam
print("총 금액:", totalPrice)  # 총 금액: 12400

sale = 0.25
totalPriceOfSale = totalPrice * (1 - sale)
print("할인 전 금액:", totalPrice, ", 할인 후 금액:", totalPriceOfSale)
