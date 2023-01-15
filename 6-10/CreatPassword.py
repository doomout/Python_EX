#안전한 함호 생성기
#사용자의 옵션에 따라 비밀번호 생성하기
#옵션에 따라 대문자, 특수문자, 숫자를 랜덤하게 생성
#최소한의 암호 길이도 설정
#생성된 문자들을 섞어야 한다.
import random
import string

print("강력한 비밀번호 생성기.")

#옵션 선택 함수
def selectOption(prompt):
    opt = " "
    #Y 나 N을 골라야 한다.
    while not opt in "YN":
        opt = input(prompt).strip().upper() 

    if opt == "Y":
        result = True
    else:
        result = False

    return result

#비밀 번호 길이 설정 함수
#최소 길이를 인수로 반환하기
def promptLength(minLen):
    #최소 길이는 0이 아니여야 함. 0이라면 1로 변환
    if minLen == 0:
        minLen = 1
    #반환 값 초기화
    result = 0
    #prompt 문장
    prompt = "비밀번호 길이는 얼마인가요? (최소=" + str(minLen) + "): "
    while result < minLen:
        #길이 묻기
        p = input(prompt).strip()
        #입력이 숫자가 맞는가?
        if p.isnumeric():
            result = int(p)
    #반환하기
    return result

#비밀번호 문자 리스티 
#섞기 쉽도록 문자열이 아닌 리스트로 저장
pwList = []

#사용할 문자 집합(소문자 집합부터 시작)
#선택한 옵션에 따라 문자 집합 추가하기
pwChars = string.ascii_lowercase

#비밀번호 최소 길이는 선택한 옵션에 따라 다름
pwMinLen = 0

#환영 메시지
print("비밀 번호 생성기")

#비밀 번호 옵션
#대문자 포함
if selectOption("대문자가 포함되어 있나요?(Y/N) "):
    #최소 길이 늘리기
    pwMinLen += 1
    #적어도 한 개의 대문자를 포함하기
    pwList.append(random.choice(string.ascii_uppercase))
    #허용된 문자 집합에 대문자 추가하기
    pwChars += string.ascii_uppercase

#숫자 포함
if selectOption("숫자가 포함되어 있나요?(Y/N) "):
    #최소 길이 늘리기
    pwMinLen += 1
    #적어도 한 개의 숫자를 포함하기
    pwList.append(random.choice(string.digits))
    #허용된 문자 집합에 숫자 추가하기
    pwChars += string.digits

#특수 문자 포함
if selectOption("특수 문자가 포함되어 있나요?(Y/N) "):
    #최소 길이 늘리기
    pwMinLen += 1
    #적어도 한 개의 특수문자를 포함하기
    pwList.append(random.choice(string.punctuation))
    #허용된 문자 집합에 특수문자 추가하기
    pwChars += string.punctuation

#비밀번호 길이 얻기
length = promptLength(pwMinLen)

#반복하며 비밀번호 문자열 생성하기
while len(pwList) < length:
    #리스트데 문자 추가하기
    pwList.append(random.choice(pwChars))

#무작위로 순서를 섞기
random.shuffle(pwList)

#리시트를 대상으로 반복하여 문자열 만들기
result = ""
for p in pwList:
    result += p

#비밀번호 출력하기
print("생성된 비밀번호 : " , result)