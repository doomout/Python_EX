#외부 텍스트 불러오기
import Strings

#플레이어 환영 메시지
def doWelcome():
    #텍스트 출력하기
    print(Strings.get("Welcome"))

#게임 출발점
def doStart():
    #텍스트 출력하기
    print(Strings.get("Start"))

    #플레이어 행동 선택
    choice = " "
    while not choice in "PSBR":
        print("-당신이 할 수 있는 일-")
        print("P = 바위 더미를 조사한다.")
        print("S = 구조물에 접근한다.")
        print("B = 삐 소리가 나는 곳으로 간다")
        print("R = 도망간다")

        choice = input("당신의 선택은?[P/S/B/R]").strip().upper()
        print("----------------------")

    #선택 처리하기
    if choice == 'P':
        doBoulders() #바위 더미 조사하기
    if choice == 'S':
        doStructure() #구조물에 접근하기
    if choice == 'B':
        doBeeping() #삐 소리가 나는 곳으로 가기
    if choice == 'R':
        doRun() #도망가기
    
#장소: 바위더미
def doBoulders():
    print(Strings.get("Boulders"))
    #시작으로 돌아가기
    doStart()

#장소: 구조물
def doStructure():
    print(Strings.get("Structure"))

    #플레이어 행동 선택
    choice = " "
    while not choice in "SDBR":
        print("-당신이 할 수 있는 일-")
        print("S = 시작 지점으로 돌아간다.")
        print("D = 문을 연다")
        print("B = 삐 소리가 나는 곳으로 간다.")
        print("R = 도망간다!")

        choice = input("당신의 선택은?[P/S/B/R]").strip().upper()
        print("-------------------------")

    #선택 처리하기
    if choice == 'S':
        doStart() #시작 지점으로 간다.
    if choice == 'D':
        doStructureDoor() #문 열기
    if choice == 'B':
        doBeeping() #삐 소리가 나는 곳으로 가기
    if choice == 'R':
        doRun() #도망가기

#장소: 구조물 입구
def doStructureDoor():
    print(Strings.get("StructurDoor"))

    choice = " "
    while not choice in "SR":
        print("당신이 할 수 있는 일:")
        print("S = 구조물로 돌아간다.")
        print("R = 도망간다!")
        choice = input("당신의 선택은?[S/R]").strip().upper()
        print("----------------------")
    
    if choice == 'S':
        doStructure()
    elif choice == 'R':
        doRun()

#장소: 삐소리 탐색하기
def doBeeping():
    pass

#도망치기
def doRun():
    print(Strings.get("Run"))
    #사망, 게임 끝내기
    gameOver()

#게임 끝내기
def gameOver():
    print(Strings.get("GameOver"))

#실제 게임 시작은 이곳에서 환영 메시지 출력하기
doWelcome()

#게임 시작하기
doStart()