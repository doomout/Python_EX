import pygame
import sys,os, random, time
from pygame.locals import * #pygame 라이브러리의 모든 지역 변수를 불러오기 위해

#게임 색상 정의 하기(상수는 대문자로 지정)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#게임 변수 초기화 하기
startSpeed = 5 #처음 이동 속도
moveSpeed = startSpeed#이동 속도 초기화
maxSpeed = 10 #최대 이동 속도
score = 0  #적 자동차가 아래에 닿으면 피한걸로 간주하고 + 1점
textFonts = ['comicsansms', 'arial']
textSize = 48
paused = False #일시 정지 상태가 아님
eNum = -1 #적 구분 변수

#게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

#게임 끝내기 함수
#메시지를 표시하고 정리하기
def GameOver():
    #게임 끝내기 문자열 만들기
    fontGameOver = pygame.font.SysFont(textFonts, textSize)
    textGameOver = fontGameOver.render("Game Over!", True, RED)
    rectGameOver = textGameOver.get_rect()
    rectGameOver.center = (IMG_ROAD.get_width()//2, IMG_ROAD.get_height()//2)
    #점수 표시하기
    fontGameOver2 = pygame.font.SysFont(textFonts, textSize//2) #글씨 사이즈 절반
    textGameOver2 = fontGameOver2.render("Score " + str(score), True, RED)
    rectGameOver2 = textGameOver2.get_rect()
    rectGameOver2.center = (IMG_ROAD.get_width()//2, IMG_ROAD.get_height()//2 + 80) #글씨 위치 
    #검은색 배경에 게임 오버 메시지 출력하기
    screen.fill(BLACK)
    screen.blit(textGameOver, rectGameOver) #게임오버 글씨 위치
    screen.blit(textGameOver2, rectGameOver2) #점수표시
    #출력 업데이트하기
    pygame.display.update()
    #객체 정리하기
    player.kill()
    enemy.kill()
    #일시 정지하기
    time.sleep(5)
    #게임 끝내기
    pygame.quit()
    sys.exit()

#게임 시작 위치
#파이 게임 초기화 하기
pygame.init()

#프레임 매니저 초기화 하기
clock = pygame.time.Clock()

#프레임 레이트 설정하기
clock.tick(60)

#이미지 불러오기
IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER,"Road.png")) #배경
IMG_PLAYER = pygame.image.load(os.path.join(IMAGE_FOLDER,"Player.png")) #플레이어 자동차
#IMG_ENEMY = pygame.image.load(os.path.join(IMAGE_FOLDER,"Enemy.png")) #적 자동차
#적 자동차 이미지 리스트
IMG_ENEMYS = []
IMG_ENEMYS.append(pygame.image.load(os.path.join(IMAGE_FOLDER,"Enemy.png")))
IMG_ENEMYS.append(pygame.image.load(os.path.join(IMAGE_FOLDER,"Enemy2.png")))
IMG_ENEMYS.append(pygame.image.load(os.path.join(IMAGE_FOLDER,"Enemy3.png")))
#장애물 이미지
IMG_ENEMYS.append(pygame.image.load(os.path.join(IMAGE_FOLDER,"IceCube.png")))


#게임 화면 초기화 하기(가로, 세로)
screen = pygame.display.set_mode((500,800)) 

#게임 객체 만들기
#플레이어 초기 위치 계산하기
h = IMG_ROAD.get_width()//2 #가로 위치는 도로 넓이의 반
v = IMG_ROAD.get_height() - (IMG_PLAYER.get_height()//2) #세로 위치는 화면의 가장 아에가 중심이 오기에 자동차 높이의 반을 뺀다.

#player 스프라이트 만들기
player = pygame.sprite.Sprite()
player.image = IMG_PLAYER 
player.surf = pygame.Surface(IMG_PLAYER.get_size())
player.rect = player.surf.get_rect(center = (h,v))



#배경 색상 결정하기
screen.fill(WHITE)

#메인 게임 루프(시작~끝까지 이 안에서 동작한다)
while True:
    #배경은 고정(이미지 복사)
    screen.blit(IMG_ROAD,(0,0))
    
    #플레이어 화면에 표시
    screen.blit(player.image, player.rect)
    
    #키보드를 눌렀을 때
    keys = pygame.key.get_pressed()
    
    #제목 표시줄 - score 표시
    pygame.display.set_caption("Crazy Driver - Score " + str(score))

    #키보드를 눌렀을 때
    keys = pygame.key.get_pressed()
    
    #일시 정지인지?
    if paused:
        #스페이스 키 확인하기
        if not keys[K_SPACE]:
            #일시 정지 끄기
            #이전 속도로 되돌리기
            moveSpeed = tempSpeed
            #일시 정지 아니라고 표시하기
            paused = False
    else:
        #왼쪽 화살표 키인지 확인하기
        if keys[K_LEFT] and player.rect.left > 0:
            #왼쪽으로 움직이기
            player.rect.move_ip(-moveSpeed, 0)
            #너무 왼쪽으로 가지 않도록 막기
            if player.rect.left < 0:
                #너무 갔다면 되돌리기
                player.rect.left = 0
        
        #오른쪽 화살표 키인지 확인하기
        if keys[K_RIGHT] and player.rect.right < IMG_ROAD.get_width():
            #오른쪽으로 움직이기
            player.rect.move_ip(moveSpeed, 0)
            #너무 오른쪽으로 가지 않도록 막기
            if player.rect.right > IMG_ROAD.get_width():
                #너무 갔다면 되돌리기
                player.rect.right = IMG_ROAD.get_width()
        #스페이스 키 확인하기
        if keys[K_SPACE]:
            #일시 정지 켜기
            #게임 속도 저장하기
            tempSpeed = moveSpeed
            #속도를 0으로 설정하기
            moveSpeed = 0
            #일시 정지 중이라 표시하기
            paused = True
    
    #적이 있는지 확인하기
    if eNum == -1:
        #무작위로 적 발생
        eNum = random.randrange(0, len(IMG_ENEMYS))

        #적 초기 위치 계산하기
        h1 = IMG_ENEMYS[eNum].get_width()//2
        hr = IMG_ROAD.get_width() - (IMG_ENEMYS[eNum].get_width()//2)
        h = random.randrange(h1, hr) #가로 위치는 랜덤
        v = 0 #세로 위치
        
        #enemy 스프라이트 만들기
        enemy = pygame.sprite.Sprite()
        enemy.image = IMG_ENEMYS[eNum]
        enemy.surf = pygame.Surface(IMG_ENEMYS[eNum].get_size())
        enemy.rect = enemy.surf.get_rect(center=(h,v))
        
    #적 화면에 표시
    screen.blit(enemy.image, enemy.rect)
    
    #적을 아래쪽으로 움직이기
    if score > 100:
        enemy.rect.move_ip(0, moveSpeed) 
    else:
        enemy.rect.move_ip(0, moveSpeed) 
    
    #적이 화면 밖(하단)으로 나갔는지 확인하기
    if (enemy.rect.bottom > IMG_ROAD.get_height()):
        #enemy 객체 없애기
        enemy.kill()
        #적 없음
        eNum = -1
        #점수 올리기
        score += 1
        #속도 올리기
        moveSpeed += 1
        #최고 속도 이하 제한
        if moveSpeed < maxSpeed:
            moveSpeed += 1    
    #충돌 확인하기
    if eNum >= 0 and pygame.sprite.collide_rect(player, enemy): #collide_rect() 두 객체가 겹치면  True반환
        #적 번호가 3인가?(얼음조각)
        if eNum == 3:
            #얼음 덩어리면 속도 되돌리기
            moveSpeed = startSpeed
        else:
            #충돌! 게임오버            
            GameOver()
        
    #이벤트 확인하기
    for event in pygame.event.get():
        #플레이어가 게임을 그만 두는가?
        if event.type == QUIT:
            #게임 끝내기
            pygame.quit()
            sys.exit()
    #화면 업데이트 하기
    pygame.display.update()