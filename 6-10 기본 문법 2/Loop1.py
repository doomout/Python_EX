animals = ["개", "개미","판다","고양이","박쥐", "염소", "개구리"]

#요소 개수만큼 루프 반복하기
for animal in animals:
    print(animal)

#숫자를 이용하여 루프 반복하기
for i in range(1, 6):
    print(i)

#2~9까지 반복
for i in range(2, 10):
    #바깥쪽 루프 반복하는 동안 1~9까지 반복
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)