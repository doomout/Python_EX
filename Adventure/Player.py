class player:
    #속성은 항상 초기화 해야 한다.
    name = "둠가이" #플레이어 이름
    livesLeft = 3 #생명력
    boulderVisits = 0 #바위 방문 횟수
    maxHealth = 100
    health = maxHealth

    #name 속성 얻기
    def getName(self): #self는 클래스의 인스턴스를 가르킨다.
        return self.name #self 인스턴스의 name 속성에 접근한다.

    #플레이어 생명력 갯수 얻기
    def getLivesLeft(self):
        return self.livesLeft

    #플레이어 죽음
    def died(self):
        if self.livesLeft > 0:
            self.livesLeft -= 1

    #플레이어가 살아있다면
    def isAlive(self):
        return True if self.livesLeft > 0 else False

    #바위 더미 방문 횟수 얻기
    def getBoulderVisits(self):
        return self.boulderVisits

    #플레이어 바위 더미 방문하기
    def visitBoulder(self):
        self.boulderVisits += 1
        
    #라이프 추가 하기
    def addLife(self):
        #라이프 늘리기
        self.livesLeft += 1
        #체력 중전하기
        self.health = self.maxHealth
        
    def addLives(self, lives):
        self.livesLeft += lives
        self.health = self.maxHealth
        
    #라이프 감소
    def loseLife(self, lives = 1):
        #목숨 줄이기
        self.livesLift -= lives
        #체력이 0 아래로 내려가지 않도록 하기
        if self.livesLeft < 0:
            #0 이하라면 0으로 지정
            self.livesLeft = 0
        #목숨이 없다면
        if self.livesLeft == 0:
            #체력도 0
            self.health = 0
        #목숨이 남았다면
        elif self.livesLeft >= 1:
            #체력은 최댓값으로 설정
            self.health = self.maxHealth
            
    #체력 더하기
    def addHealth(self, health):
        self.health += health
        #maxHealth를 넘지 않도록
        if self.health > self.maxHealth:
            #더 높아지면 최댓값으로
            self.health = self.maxHealth
    
    #체력 잃기
    def loseHealth(self, health):
        self.health -= health
        #0 아래로 내려가지 않도록
        if self.health < 0:
            #라이프 잃기
            self.loseLife()