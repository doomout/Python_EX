import pygame
import sys
from pygame.locals import * #pygame 라이브러리의 모든 지역 변수를 불러오기 위해

#게임 색상 정의 하기(상수는 대문자로 지정)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#게임 시작 위치
#파이 게임 초기화 하기
pygame.init()

#프레임 매니저 초기화 하기
clock = pygame.time.Clock()

#프레임 레이트 설정하기
clock.tick(60)

#제목 표시줄 설정하기
pygame.display.set_caption("Crazy Driver")

#게임 화면 초기화 하기(가로, 세로)
screen = pygame.display.set_mode((500,800)) 

#배경 색상 결정하기
screen.fill(WHITE)

#메인 게임 루프(시작~끝까지 이 안에서 동작한다)
while True:
    #이벤트 확인하기
    for event in pygame.event.get():
        #플레이어가 게임을 그만 두는가?
        if event.type == QUIT:
            #게임 끝내기
            pygame.quit()
            sys.exit()
    #화면 업데이트 하기
    pygame.display.update()