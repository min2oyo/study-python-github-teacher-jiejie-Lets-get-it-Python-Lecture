print("미세먼지 저감 조치에 따른 차량 2부제를 시행합니다!")

odd = "홀수"
even = "짝수"
str1 = ""
str2 = ""

date = int(input("날짜: "))

if date < 31:
    if date % 2:
        str1 = odd
        str2 = even
    else:
        str1 = even
        str2 = odd
    print(str1, "번호 차량만 통행 가능합니다.")
    print(str2, "번호 차주는 오늘 대중교통을 이용하세요.")
else:
    print("올바른 날짜를 입력하세요.")
