#생일 카운트 다운 프로그램
#기본 로직 오늘 날짜 - 입력 날짜
import datetime

#오늘 날짜 알아내기 
today = datetime.datetime.now()

print(today)
#생년월일 입력 받기
year = int(input("생년월일 입력(년):"))
month = int(input("생년월일 입력(월):"))
day = int(input("생년월일 입력(일):"))

#입력 받은 데이터 처리
dday = today - datetime.datetime(year,month,day) 

#생일 카운트 하기
if today.month == month and today.day == day:
    print("오호? 당신 오늘 생일임? 축하합니다~")
else:
    #오늘의 월보다 생일월이 작거나 (월은 같지만 생일의 일이 크다면)
    if today.month > month or (today.month == month and today.day > day):
        year = year + 1 #년도을 1년 플러스 한다.
    else:
        year = today.year #올해년을 표시한다.

#생일의 남은 날을 출력한다.
print("당신의 생일은 ", datetime.datetime(year,month,day) - today,"일 남았습니다.")
#출력하기 살아온 날
print("당신이 지금까지 살아온 날은",dday, "일 입니다.")