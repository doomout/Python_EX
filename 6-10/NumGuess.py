import random

#변수 정의하기
guesses = 0  #시도 횟수 저장
numMin = 1 #범위 시작 숫자
numMax = 100 #범위 끝 숫자
userInput = "" #사용자 입력 저장
userGuess = 0  #사용자 입력 숫자로 저장

#무작위 숫자 저장
randNum = random.randrange(numMin, numMax+1)

#게임 설명하기
print("컴퓨터가", numMin, "~", numMax, "사이의 숫자 하나를 정했습니다.")
print("이 숫자는 무엇일까요?")

#사용자가 맞힐 때까지 반복
while randNum != userGuess:
    #사용자 답 입력받기
    userInput = input("예상 숫자: ").strip()
    #숫자가 아닌 값을 입력했다면...
    if not userInput.isnumeric():
        print(userInput, "숫자를 입력하시요 ㅡㅡ")
    else:
        #시도 횟수 1회 늘리기
        guesses = guesses + 1
        #입력한 값을 숫자로 변환
        userGuess = int(userInput)
        #숫자 확인하기
        if userGuess < numMin or userGuess > numMax:
            print(userGuess, "은 ", numMin, "와", numMax, "사이가 아닙니다.")
        elif userGuess < randNum:
            print("숫자가 작습니다. 다시 입력하세요.")
        elif userGuess > randNum:
            print("숫자가 큽니다. 다시 입력하세요.")
        else:
            print("드디어 ", guesses,"회만에 정답이네요 ㅋㅋㅋㅋ")

print("빠이요~!")