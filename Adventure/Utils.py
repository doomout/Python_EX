import random

#선택지 리스트와 선택 프롬프트를 출력하고 사용자 선택을 반환한다.
#[["문자", "출력 텍스트"]]와 같이 리스트로 이루어진 리스트 형식으로 전달한다.
#선택한 문자를 반환한다.
def getUserChoice(options):
    #유효한 입력 목록에 선택 가능한 문자 추가하기
    validInputs = ""
    #선택지 루프
    for opt in options:
        #유요한 입력 목록에 선택 가능한 문자 추가하기
        validInputs += opt[0]
        #출력하기
        print(opt[0], "-", opt[1])

    #프롬프트 만들기
    prompt = "당신의 선택은?["+validInputs+"]: "
    #변수 초기화 하기
    choice = ""
    done = False
    #메인 루프
    while not done:
        #대문자 하나 가져오기
        choice = input(prompt).strip().upper()
        #사용자가 2자 이상 입력했다면
        if len(choice) > 1:
            #첫 문자만 사용
            choice = choice[0]
        #입력한 문자 확인
        if len(choice) == 1 and choice in validInputs:
            #맞다면 반복 빠져 나가기
            done = True

    #선택한 옵션 반환하기    
    return choice

'''
#테스트 코드
choices = [
    ["A", "A 선택"],
    ["B", "B 선택"],
    ["C", "C 선택"],
    ["3", "그리고 숫자 하나"]
]
choice = getUserChoice(choices)
print(choice)
'''

#무작위 이벤트가 발생할 확율 함수
#발생 빈도 전달하기(2: 2번 중 1번, 3: 3번중 1번 등)
def randomEvent(freq):
    return True if random.randrange(0, freq) == 0 else False