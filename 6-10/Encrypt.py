#사용할 아스키 범위 - 이 범위를 벗어나면 오류가 발생할 수 있다.
asciiMin = 32 #공백문자
asciiMax = 126 #물결표 문자 ~

#암호화 키
key = 314159
key = str(key) #각 문자에 접근할 수 있도록 문자열로 변환

#암호화할 메시지 입력 받기
message = input("암호화할 메세지를 입력하시요: ")

#암호화할 메시지용 변수 초기화 하기
messEncr = ""

#받은 문자열의 길이만큼 반복하기
for index in range(0, len(message)):
    #해당문자의 아스키값 가져오기
    char = ord(message[index])
    #이 문자가 범위 밖인가?
    if char < asciiMin or char > asciiMax:
        #이 문자는 암호화에 적당하지 않으니 그대로 입력한다.
        messEncr += message[index]
    else:
        #이 문자는 암호화해도 안전하다
        #키만큼 값을 더해서 암호화 한다.
        ascNum = char + int(key[index % len(key)])
        #더한 값이 범위를 벗어나면 범위 처음으로 되돌린다.
        if ascNum > asciiMax:
            ascNum -= (asciiMax - asciiMin)
        #문자로 변환하고 출력할 내용에 추가한다.
        messEncr = messEncr + chr(ascNum)


#결과 출력하기
print("암호화된 메시지: ", messEncr)