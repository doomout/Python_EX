#리스트 만들기
animals = ["개", "개미","판다","고양이","박쥐", "염소", "개구리"]

print(animals)
#요소의 개수 묻기
print(len(animals), "종류의 동물이 리스트에 있습니다.")
animals[6] = "토끼" #개구리를 토끼로 바꿈
print(animals)
animals.append("여우") #여우를 마지막 요소에 추가한다.
print(animals)
animals.pop(2) #인덱스를 사용해서 2번째 요소 삭제(개미)
print(animals)
animals.remove("고양이") #요소의 값으로 삭제(고양이)
print(animals)

#리스트에서 요소 값으로 찾기
if "염소" in animals:
    print("리스트에 염소가 있다.", animals.index("염소"), "번에 염소가 있다")
else:
    print("리스트에 염소가 없다.")

#리스트 정렬하기
animals.sort()
print(animals)