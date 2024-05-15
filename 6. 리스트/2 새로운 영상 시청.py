history = []

for i in range(5):
    history.append(input("시청한 영상은? "))

print("지금까지 시청한 영상은,", history)

if "다이어트" in history:
    print("다이어트 영상을 좋아하시면 홈트레이닝 영상도 좋아하실 것 같아요!")
if "늇스" in history:
    print("뉴스 영상을 좋아하시면 속보 영상을 추천합니다!")
