# Python 정리 
현재 사용 파이썬 버전 : 3.11.1   
사용 IDE :  VS Code  
공부 중인 도서 : Do it! 게임 10개 만들며 배우는 파이썬  
--문법--  
1. 출력 - print("출력할 텍스트")   
2. 주석 -  # 사용  
3. 입력 - input("입력하세요: ")  
4. 변수 선언시 "" 넣으면 문자열로, 없으면 숫자로 인식하여 자료형을 따로 지정하지 않아도 된다.  
5. 문자열에서는 +는 문자 연결, 그 이외는 + 연산자  
6. 외부 라이브러리는 import 로 연결  
7. random.randrange(1, 11) //1~10까지의 수 중 랜덤, 11인 이유: 1은 이상, 11은 미만이기에 10까지 표현  
8. random.choice(리스트명) // 리스트에 지정된 데이터를 랜덤하게 선택하여 출력  
9. 리스트 선언법 - 리스트명  = ["값1", "값2", "값3", "값4", "값5"]  //리스트에는 어떠한 형식이든 넣을 수 있다.   
10. 연산자 - // 나눗셈 연산자 나머지 없이 몫만 출력  
11. 연산자 - % 나머지 연산자 나머지를 구할 때 사용   
12. 조건문 - 파이썬은 {} 대신 :를 사용한다.  
            if, elif, else를 사용한다.  
```py
#if today.weekday() in [5,6]: 으로 줄일 수도 있다.  
if today.weekday() == 6 or today.weekday() == 5:  
      print("주말이니 회사에 가지 않아!!")  
      print("온종일 신나게 놀즈아~!")  
elif today.weekday() == 4:   
      print("예아!! 오늘은 불금이다!!!")  
else:   
      print("오늘은 회사 가는 날....")  
```
13. 형변환 - 문자열에서 int 자료형으로 변환 한다면  
    year = "2023" //문자열로 저장  
    year = int("2023") // int형으로 변환되어 int형으로 저장  
14. 문자열 공백 없애기 - rstrip(): 오른쪽 공백 삭제, lstrip(): 왼쪽 공백 삭제, strip(): 앞뒤 공백 삭제  
15. len() 함수 - 리스트에 요소가 몇개 있는지, 문자열의 길이를 확인하는 함수  
16. 리스트의 추가/삭제 : append("값") - 리스트 끝에 요소 추가, pop(인덱스 값) - 인덱스 값을 사용하여 삭제, remove("값") - 요소 값으로 삭제  
17. 요소 개수만큼 루프 반복   
```py
animals = ["개", "개미","판다","고양이","박쥐", "염소", "개구리"]  
for animal in animals:    
      print(animal)    
```
18. 숫자를 이용하여 반복  
```py
for i in range(1, 11):  
      print(i)
```
19. if 문에서 반대 조건 방법
```py
if not userInput.isnumeric(): #숫자가 아닌 값이 입력되면...
      print(userInput, "숫자를 입력하시요 ㅡㅡ")
```
20. 함수 선언법  
```py
#Hello를 출력하는 함수(인수가 없는 경우)
def sayHello(): #def는 define의 줄임말이다.
      print("Hello")

sayHello() #Hello 출력

#숫자 2개를 곱하고 출력하는 함수(인수가 있는 경우)
def multiply(n1, n2)
      print(n1, "x", n2, "=", n1 * n2)

multiply(10, 5) #10x5=50 출력
```
21. 빈 함수 만들기 : 세부 구현 전에 구조 잡을 때 아래와 같이 선언하면 오류가 나지 않는다.
```py
def doBeeping():
    pass 
```
22. 딕셔너리 만들기 : {}를 사용하여 키 : 값 으로 이루어진 자료형, 리스트는 [] 로 감싼다.
```py
pet = {
    "animal" : "Iguana",
    "name" : "Iggy",
    "food" : "Veggies",
    "mealsPerDay" : 1
}
pet["mealsPerDay"] = 2 #값을 2로 재할당
pet.update({"mealsPerDay":2}) #이와 같이 변경도 가능
clear()  #모든 요소를 삭제
copy()   #요소 복사
keys()   #모든 키를 리스트로 반환
values() #모든 값을 리스트로 반환
```
23. 직렬화란? 데이터 직렬화란 변수, 리스트, 클래스, 딕셔너리 등의 파이썬 객체를 저장할 수 있는 바이트 문자열로 바꾸는 것  
    역직렬화란? 그 반대로 바이트 문자열을 다시 파이썬 객체로 바꾸는 것   
24. 파일 저장하려면 pickle라는 파이썬 라이브러리를 사용해야 한다.
```py
from os import path
import pickle

#데이터 파일
saveDataFile = "saveFile.p"

#데이터 객체 만들기
db = {
      "inv" : inv,
      "player" : player
}
#저장하기
pickle.dump(db, open(saveDataFile, "wb")) #wb는 데이터 쓰기 모드

#저장한 파일 읽기
if path.isfile(saveDataFile): #저장한 파일이 있는가?
      db = pickle.load(open(saveDataFile, "rb")) #rb는 데이터 읽기 모드
      inv = db["inv"]
      player = db["player"]
```
25. pygame 설치하기
현재 파이썬 최신 버전인 3.11.1에선 pygame가 설치 되지 않는다. 그래서 pre버전을 설치해야 한다.  
맥 os : pip3 install pygame --pre   
26. 튜플이란? 값이 변하지 않는 상수 ()로 지정한다. 튜플은 대문자로 입력하여 구분하는게 좋다.
```py
#색상을 정의 하는 코드[리스트]
red = [255,0,0]
#색상을 정의 하는 코드(튜플)
RED = (255,0,0)
```
27. 프레임 레이트란? 게임을 플레이 할 때 화면이 바뀌는 빈도는 FPS로 나타내며, 
    이 값을 프레임 레이트라고 한다. 이 값이 높을수록 게임이 자연스럽지만 프로세스 점유율이 높아진다.  
28. 살행하는 코드의 경로를 알 수 있는 방법
```py
import os #운영체제에 관한 함수 라이브러리
#게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")
print("게임 루트:" , GAME_ROOT_FOLDER)
print("이미지 폴더:", IMAGE_FOLDER)
```
29. 스프라이트란? 큰 이미지 위에 놓인 2차원 이미지를 뜻함. 스프라이트는 표시하거나 숨길수 있고, 움직이거나 회전할 수도 있다.  
    자동차는 움직여야 하니 스프라이트로 만든다.
