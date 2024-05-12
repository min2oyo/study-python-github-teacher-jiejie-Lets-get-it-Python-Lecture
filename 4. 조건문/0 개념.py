age = int(input("나이: "))

if age > 19:
    print("성인은 주류를 구매할 수 있습니다.")

if age < 20:
    print("미성년자는 주류를 구매할 수 없습니다.")
    print(20 - age, "년 후에 성인이 되면 오세요!")

print("감사합니다. 안녕히 가세요.")
