#테두리와 함께 텍스트를 출력하는 함수
def displayWelcome(txt):
    borderChar = "*" #테두리 문자
    print(borderChar * (len(txt) + 4)) #맨 위 줄
    print(borderChar, txt, borderChar) #가운데 줄
    print(borderChar * (len(txt) + 4)) #맨 아래 줄

#함수 테스트 하기
displayWelcome("Welcome to Coding Hell")

#숫자 입력 함수
def inputNumber(prompt):
    #입력 변수
    inp= ""
    #변수가 유요한 숫자일 때까지 반복하기
    while not inp.isnumeric():
        #입력
        inp = input(prompt).strip()
    #숫자 반환하기
    return int(inp)

#숫자 가져오기
num = inputNumber("숫자 입력: ")
#출력하기
print(num)