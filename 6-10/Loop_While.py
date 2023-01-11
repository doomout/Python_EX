#빈 리스트 만들기
animals = []

#입력 변수 초기화하기
userInput = " "

print("animals 리스트를 만들어 봅시다")
print("한번에 하나씩 동물을 입력하세요.")
print("입력을 끝내려면 빈칸을 입력하세요.")

#빈 문자열이 될 때까지 반복
while userInput != "":
    userInput = input("동물의 종류를 입력하세요. 끝내려면 빈칸으로 두세요: ").strip()
    #있다면 추가함
    if len(userInput) > 0:
        animals.append(userInput)

#데이터 정렬하기
animals.sort()

#리스트 출력하기
print(animals)