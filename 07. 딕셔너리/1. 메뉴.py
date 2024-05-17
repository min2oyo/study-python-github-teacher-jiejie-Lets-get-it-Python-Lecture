menu = {"김밥": 2500, "참치김밥": 3500, "라면": 3000, "치즈라면": 4000}

print(menu[input("메뉴: ")], "원입니다.")


name = input("\n메뉴 추가: ")
menu[name] = int(input("메뉴 가격: "))

print(menu)
