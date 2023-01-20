import pygame

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

#화면 업데이트 하기
pygame.display.update()