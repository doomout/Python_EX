import random
cChoice = random.choice("SRP")

print("가위, 바위, 보?")
uChoice = input("S(가위), R(바위), P(보) 중 하나를 고르세요: ").upper().strip() #대문자로 변환하고, 앞뒤 공백 제거

print("나: ", uChoice)
print("컴퓨터: ", cChoice)

#선택 비교 하기
if cChoice == uChoice:
    print("무승부!")
elif uChoice == "R" and cChoice == "P":
    print("당신이 고른 것은 바위(R), 컴이 고른 것은 보(P). 당신이 졌엌ㅋㅋㅋ")
elif uChoice == "P" and cChoice == "R":
    print("당신이 고른 것은 보(P), 컴이 고른 것은 바위(R). 오~! 당신이 이겼네??")
elif uChoice == "R" and cChoice == "S":
    print("당신이 고른 것은 바위(R), 컴이 고른 것은 가위(S). 당신이 이겼어")
elif uChoice == "S" and cChoice == "R":
    print("당신이 고른 것은 가위(S), 컴이 고른 것은 바위(R). 당신이 졌어 ㅋ")
elif uChoice == "P" and cChoice == "S":
    print("당신이 고른 것은 보(P), 컴이 고른 것은 가위(S). 당신이 졌어 ㅋㅋㅋ")
elif uChoice == "S" and cChoice == "P":
    print("당신이 고른 것은 가위(S), 컴이 고른 것은 보(P). 오~! 당신이 이겼네??")
else:
    print("이게 뜨면 당신이 다른 걸 누른거지 뭐 ㅡㅡ")