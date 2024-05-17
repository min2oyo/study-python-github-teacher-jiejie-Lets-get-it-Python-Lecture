"""
1. 자기소개
"""

print("나는 " + input("당신은 누구입니까?") + "이다.")  # 전설 # 나는 전설이다.


"""
2. 회원가입
"""

id = input("ID: ")  # yoori
name = input("이름: ")  # 유리

print(name, "님! 회원가입을 환영합니다!")  # 유리님! 회원가입을 환영합니다!
print(
    id, "님에게 지금 즉시 사용 가능한 쿠폰 5개 발급!"
)  # yoori님에게 지금 즉시 사용 가능한 쿠폰 5개 발급!
print(id, "님에게만 적립금 2000원 추가 지급!")  # yoori님에게만 적립금 2000원 추가 지급!


"""
4. 점수
"""

rateOfKorean = 0.16  # 80
rateOfMath = 0.34  # 60
rateOfEnglish = 0.23  # 93

korean = int(input("국어: "))
math = int(input("수학: "))
english = int(input("영어: "))

score = korean * rateOfKorean + math * rateOfMath + english * rateOfEnglish

print("최종 점수는", score, "입니다!")  # 최종 점수는 54.59 입니다!
