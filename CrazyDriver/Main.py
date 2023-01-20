import pygame
import sys,os, random
from pygame.locals import * #pygame 라이브러리의 모든 지역 변수를 불러오기 위해

#게임 색상 정의 하기(상수는 대문자로 지정)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#게임 변수 초기화 하기
moveSpeed = 5

#게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

#게임 시작 위치
#파이 게임 초기화 하기
pygame.init()

#프레임 매니저 초기화 하기
clock = pygame.time.Clock()

#프레임 레이트 설정하기
clock.tick(60)

#제목 표시줄 설정하기
pygame.display.set_caption("Crazy Driver")

#이미지 불러오기
IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER,"Road.png")) #배경
IMG_PLAYER = pygame.image.load(os.path.join(IMAGE_FOLDER,"Player.png")) #플레이어 자동차
IMG_ENEMY = pygame.image.load(os.path.join(IMAGE_FOLDER,"Enemy.png")) #적 자동차

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

#적
#적 초기 위치 계산하기
h1 = IMG_ENEMY.get_width()//2
hr = IMG_ROAD.get_width() - (IMG_ENEMY.get_width()//2)
h = random.randrange(h1, hr) #가로 위치는 랜덤
v = 0 #세로 위치

#enemy 스프라이트 만들기
enemy = pygame.sprite.Sprite()
enemy.image = IMG_ENEMY
enemy.surf = pygame.Surface(IMG_ENEMY.get_size())
enemy.rect = enemy.surf.get_rect(center=(h,v))

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
    
    #적 화면에 표시
    screen.blit(enemy.image, enemy.rect)
    
    #적을 아래쪽으로 움직이기
    enemy.rect.move_ip(0, moveSpeed) 
    
    #화면 밖으로 나갔는지 확인하기
    if (enemy.rect.bottom > IMG_ROAD.get_height()):
        #그렇다면 다시 위로 보내기
        #enemy.rect.top = 0
        #새로 무작위 위치 계산하기
        hl = IMG_ENEMY.get_width()//2
        hr = IMG_ROAD.get_width() - (IMG_ENEMY.get_width()//2)
        h = random.randrange(hl, hr)
        v = 0
        #화면에 표시
        enemy.rect.center = (h, v)
    #이벤트 확인하기
    for event in pygame.event.get():
        #플레이어가 게임을 그만 두는가?
        if event.type == QUIT:
            #게임 끝내기
            pygame.quit()
            sys.exit()
    #화면 업데이트 하기
    pygame.display.update()