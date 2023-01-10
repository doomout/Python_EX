import datetime

today = datetime.datetime.now()

 #요일에 해당하는 숫자를 반환(0:월요일,1:화요일, ..., 6:일요일)
if today.weekday() == 6 or today.weekday() == 5: #일요일(6)이거나, 토요일(5)일 때
    print("주말이니 회사에 가지 않아!!")
    print("온종일 신나게 놀즈아~!")
elif today.weekday() == 4: #금요일(4)이라면??
    print("예아!! 오늘은 불금이다!!!")
else: #나머지 요일
    print("오늘은 회사 가는 날....")