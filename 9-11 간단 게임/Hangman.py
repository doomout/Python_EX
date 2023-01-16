#라이브러리 불러오기
import random

#변수 초기화 하기
maxLives = 7 #최대 허용 추측 횟수
maskChar = "_" #마스킹 문자
liveUsed = 0 #시도 횟수
guessedLetters = [] #사용자 추측 문자를 저장할 리스트

#게임 단어 리스트
gameWords = ["anvil", "boutique", "cookie", "fluff", 
            "jazz", "pneumonia", "sleigh", "society", 
            "topaz", "tsunami", "yummy", "zombie"]

#게임에 사용할 리스트
gameWord = random.choice(gameWords)

#전체를 마스킹한 문자열로 시작하기
displayWord = maskChar * len(gameWord)

#게임 시작하기, 단어를 맞추거나 최대 횟수에 이를떄까지 반복
while gameWord != displayWord and liveUsed < maxLives:
    #먼저 마스킹한 단어 출력하기
    print(displayWord)

    #다음으로 이미 추측한 문자 표시하기
    #보기 좋게 리스트를 문자열로 만들기
    #이미 추측한 문자가 있는지?
    if len(guessedLetters) > 0:
        #입력한 내용이 있다면 빈 분자열로 시작하기
       youTried = ""
       #추측한 각 문자 더하기
       for letter in guessedLetters:
            youTried += letter    
            print("시도한 문자:", youTried)
    #남은 시도 횟수 출력하기
    print(maxLives - liveUsed, "번 남았습니다.") 
    #보기 좋게 빈 줄 출력하기
    print()

    #추측 문자 입력받기
    currGuess = input("추측 문자:").strip().lower()
    #1자만 받기
    if len(currGuess) > 1:
        currGuess = currGuess[0]
        #같은 문자 반복 추측 방지하기
        if currGuess in guessedLetters:
            print("이미 추측한 문자입니다:",currGuess)
        else:
            #새로운 추측 문자이므로 추측 문자 리스트에 저장하기
            guessedLetters.append(currGuess)
            #리스트 정렬하기
            guessedLetters.sort()

            #마스킹 업데이트 하기
            #빈 문자열로 시작하기
            displayWord = ""
            #1자씩 루프하기
            for letter in gameWord:
                #필요한 마스킹 또는 문자 추가하기
                #추측한 문자가 맞는지?
                if letter in guessedLetters:
                    #맞힌 문자이므로 출력할 문자열에 추가하기
                    displayWord += letter
                else:
                    #아직 맞히지 않은 문자는 마스킹하기
                    displayWord += maskChar
        
        #올바른 추측인가요?
        if currGuess in gameWord:
            #정답이라면
            print("올바른 추측입니다.")
        else:
            #정답이 아니라면
            print("틀렸습니다.")
            #시도 횟수 1회 늘리기
            liveUsed += 1
    #보기 좋게 빈 줄 출력하기
    print()

#게임 끝내고 결과 출력하기
if displayWord == gameWord:
    #이겼다면
    print("당신이 이겼어... 단어는",gameWord, "입니다!")
else:
    #졌다면
    print("여러분이 졌습니다. 정답은:", gameWord)