#플레이어 환영 메시지
def doWelcome():
    #텍스트 출력하기
    print("크흐흐흐 당신은 이미 아무런 기억이 없지")
    print("당신이 누구인지 알고 싶은가??")
    print("당신을 알아가는게 이 게임의 시작이라네.")
    print("-------------------------------")

#게임 출발점
def doStart():
    #텍스트 출력하기
    print("주위를 둘러보니 어둡기만 하다")
    print("주위에 바위 더미가 있다.")
    print("또한 이상하게 생긴 구조물도 있다.")
    print("어디선가 삐 소리가 난다.")
    print("----------------------------")

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
    print("정말인가요? 그건 바위 더미입니다.")
    print("크고 무겁고 단순한 바위입니다.")
    print("--------------------------")
    #시작으로 돌아가기
    doStart()

#장소: 구조물
def doStructure():
    print("이상한 구조물을 조사한다.")
    print("안에서 사악한 소리가 들린다.")
    print("문이 보인다.")
    print("문을 열어보니 끼이익 소리가 들린다.")
    print("---------------------------")

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
    print("문은 잠긴 듯하다.")
    print("둥근 구멍이 보인다. 열쇠 구멍인가?")
    print("열려고 시도하지만 안된다.")
    print("---------------------------")

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
    print("비명을 지르며 도망친다.")
    print("갑자기 악마가 나타나서 당신에게 샷건을 쏩니다.")
    print("플레이어가 사망 했습니다.")
    print("-----------------------------------")
    #사망, 게임 끝내기
    gameOver()

#게임 끝내기
def gameOver():
    print("게임 오버!")
    print("------------")

#실제 게임 시작은 이곳에서 환영 메시지 출력하기
doWelcome()

#게임 시작하기
doStart()