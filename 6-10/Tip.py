#서비스 팁 계산 프로그램

#영수증 값 입력
bill = float(input("음식값을 입력하시요:"))

#지금하고자 하는 팁 %입력
tipPercent = float(input("지급하고 싶은 팁의 %를 입력하시요:"))

#계산 하기
tip = bill / 100 * tipPercent

total = bill + tip
#출력
print("음식값: ", bill)
print("팁:",  round(tip, 2)) #소수점 2자리 이후는 반올림
print("총 지불 값: ", round(total, 2) ) #소수점 2자리 이후는 반올림