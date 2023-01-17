#외부 텍스트 불러오기
import Strings
import Utils
import Inventory as inv #Inventory를 줄이고자 inv로 별칭을 지정한다.
import Player

#player 객체 생성하기
p = Player.player()

#플레이어 환영 메시지
def doWelcome():
    #텍스트 출력하기
    print(Strings.get("Welcome"))

#게임 출발점
def doStart():
    #텍스트 출력하기
    print(Strings.get("Start"))

    #플레이어가 선택할 수 있는 해동은?
    choices = [["P", "바위 더미를 조사한다."],
               ["S", "구조물에 접근한다."],
               ["B", "삐 소리가 나는 곳으로 간다"],
               ["R", "도망간다"],
               ["I", "인벤토리"] ]
    choice = Utils.getUserChoice(choices)
    #선택 처리하기
    if choice == 'P':
        doBoulders() #바위 더미 조사하기
    if choice == 'S':
        doStructure() #구조물에 접근하기
    if choice == 'B':
        doBeeping() #삐 소리가 나는 곳으로 가기
    if choice == 'R':
        doRun() #도망가기
    if choice == 'I':
        inv.display()
        doStart()
    
#장소: 바위더미
def doBoulders():
    #이 방문 추적하기
    p.visitBoulder()
    
    #텍스트 출력하기 3번 방문하면 열쇠를 찾는다.
    if p.getBoulderVisits() == 1:
        print(Strings.get("Boulders")) #평범한 바위 설명 출력하기
    elif p.getBoulderVisits() == 3:
        print(Strings.get("BouldersKey")) #키를 발견한 설명 출력하기
        inv.takeStructureKey()
    else:
        print(Strings.get("Boulders2")) #평범한 바위 설명 출력하기2
    
    #시작으로 돌아가기
    doStart()

#장소: 구조물
def doStructure():
    print(Strings.get("Structure"))

    #플레이어가 선택할 수 있는 해동은?
    choices = [["S", "시작 지점으로 돌아간다."],
               ["D", "문을 연다"],
               ["B", "삐 소리가 나는 곳으로 간다."],
               ["R", "도망간다!"] ]
    choice = Utils.getUserChoice(choices)
   
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

    #열쇠가 있을 때 출력
    if inv.hasStructureKey():
        print(Strings.get("StructureDoorKey"))
    else:
        print(Strings.get("StructureDoorNoKey"))

    #플레이어가 선택할 수 있는 해동은?
    choices = [["S", "구조물로 돌아간다."],
               ["R", "도망간다!"] ]
    #플레이어는 열쇠를 가졌는가?
    if inv.hasStructureKey():
        choices.insert(0, ["U", "문 열쇠 풀기"])

    #플레이어 행동 선택 프롬프트
    choice = Utils.getUserChoice(choices)

    if choice == 'S':
        doStructure()
    elif choice == 'R':
        doRun()
    elif choice == 'U':
        doEnterStructure()

def doEnterStructure():
    pass

#장소: 삐소리 탐색하기
def doBeeping():
    pass

#도망치기 도망 갈 때 마다 생명력 -1개 0개 되면 사망
def doRun():
    #텍스트 출력
    print(Strings.get("Run"))
     #생명력 -1씩 처리
    p.died()
    #생명력이 남아 있나?
    if p.isAlive():
        print(p.livesLeft, "개의 생명력이 남았습니다.\n"
              "--------------------------------") #생명력 표시 하기
        doStart()
    else:
        print("당신의 생명력이 다 했습니다.\n"
              "--------------------------")
        #사망, 게임 끝내기
        gameOver()

#게임 끝내기
def gameOver():
    print(Strings.get("GameOver"))

#실제 게임 시작은 이곳에서 환영 메시지 출력하기
doWelcome()

#게임 시작하기
doStart()


