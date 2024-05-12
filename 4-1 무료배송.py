minOrderPrice = 20000
minFreeDeliveryPrice = 50000
deliveryCharge = 2500
price = 0

inputPrice = int(input("구매가격: "))

if inputPrice < minOrderPrice:
    print("주문금액", minOrderPrice - inputPrice, "원이 부족합니다.")
else:
    if inputPrice < minFreeDeliveryPrice:
        price += deliveryCharge
        print("배송비", deliveryCharge, "원이 추가됩니다.")
    else:
        print("무료배송입니다.")
    price += inputPrice
    print("최종 결제금액은", price, "입니다.")
