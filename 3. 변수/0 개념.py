"""
1. 변수
"""

a = 10
print(a)  # 10

b = "학생"
c = "고등"
print(c + b)  # 고등학생


c = "대"
print(c + b)  # 대학생

name = "유리"
height = 175.5
age = 21
hobby = "programming"
print(
    name, "키는", height, ", 나이는", age, ", 취미는", hobby, "입니다!"
)  # 유리 175.5 21 programming

name = "제임스"
height = 186
age = 24
hobby = "요리하기"
print(
    "{} 키는 {}, 나이는 {}, 취미는 {}입니다!".format(name, height, age, hobby)
)  # 제임스 키는 186, 나이는 24, 취미는 요리하기입니다!


"""
2. 주석
원의 넓이를 구하는 프로그램입니다.
변수 p는 원주율을 저장한 변수이고,
변수 r은 반지름을 저장한 변수입니다.
"""

p = 3.141592
r = 10
# r = int(input("반지름: "))  # 10

lengthOfCircle = 2 * p * r
areaOfCircle = p * r**2
areaOfSphere = 4 * p * r**2

print("원의 길이 =", lengthOfCircle)  # 원의 길이 = 62.83184
print("원의 넓이 =", areaOfCircle)  # 원의 넓이 = 314.1592
print("구의 겉넓이 =", areaOfSphere)  # 구의 겉넓이 = 1256.6368


"""
3. 데이터 타입
"""

year = 2016
print(type(year))  # <class 'int'>

height = 175.5
print(type(height))  # <class 'float'>

name = "제임스"
print(type(name))  # <class 'str'>


"""
4. 데이터 타입 바꾸기
"""

score = 79
print(type(score), score)  # <class 'int'> 79
score = float(score)
print(type(score), score)  # <class 'float'> 79.0

avg = 84.3
print(type(avg), avg)  # <class 'float'> 84.3
avg = int(avg)
print(type(avg), avg)  # <class 'int'> 84

x = 32
y = 32.9
x = str(x)
y = str(y)
print(type(x), type(y))  # <class 'str'> <class 'str'>
print(x + y)  # 3232.9

a = "30"
print(type(a))  # <class 'str'>
a = int(a)
print(type(a), a * 3)  # <class 'int'> 90
