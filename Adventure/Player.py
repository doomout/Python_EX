class player:
    #속성은 항상 초기화 해야 한다.
    name = "둠가이" #플레이어 이름
    livesLeft = 3 #생명력
    boulderVisits = 0 #바위 방문 횟수

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