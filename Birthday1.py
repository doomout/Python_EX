import datetime

#사용자 입력 얻기 int()는 문자열을 int로 형변환 한다는 것
year = input("태어난 해는 언제인가?")
year = int(year)
month = input("태어난 달은 언제인가?")
month = int(month)
day = input("태어난 날은 언제인가?")
day = int(day)

#날짜 만들기
bday = datetime.datetime(year, month, day)

 #요일에 해당하는 숫자를 반환(0:월요일,1:화요일, ..., 6:일요일)
if bday.weekday() == 6:
    dow = "일"
elif bday.weekday() == 0:
    dow = "월"
elif bday.weekday() == 1:
    dow = "화"
elif bday.weekday() == 2:
    dow = "수"
elif bday.weekday() == 3:
    dow = "목"
elif bday.weekday() == 4:
    dow = "금"
elif bday.weekday() == 5:
    dow = "토"

#결과 출력하기
print("태어난 날은", dow,"요일이군요.")
