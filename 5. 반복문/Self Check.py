"""
1. 반복문
"""

for i in range(1, 11):
    print(i * 10)


"""
2. 홈트레이닝 계획
"""

print("홈트레이닝 2주 계획입니다.")
for i in range(1, 15):
    if i % 5:
        print(i, "일: 스쿼트 - 윗몸 일으키기 - 유산소 운동")
    else:
        print(i, "일: 휴식일입니다.")


"""
3. 후라이팬 놀이
"""

print("\n팅 팅팅팅 탱 탱탱탱 팅팅 탱탱 후라이팬 놀이!")

for i in range(5):
    print("\n횟수", i + 1, "/", 5)
    name = input("이름: ")
    count = int(input("횟수: "))
    answer = input("답변: ")

    if name * count != answer:
        print("떙! 답은: ", name * count)
        break
