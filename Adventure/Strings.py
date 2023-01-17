#문자열 외부화 하기

def get(id):
    if id == "Welcome":
        return ("당신은 어떤 곳에 떨어졌습니다.\n"
                "여기가 어디인지 황당합니다.\n"
                "근처에 뭐가 있는지 둘러봅니다.")
    elif id == "Start":
        return ("주위엔 붉은 사망과 바위 더미가 있습니다.\n"
                "저기 앞에 이상하게 생긴 구조물이 있다.\n"
                "가까이 가니 어떤 소리가 난다.")
    elif id == "Boulders":
        return ("정말인가요?? 그건 바위 더미입니다.\n"
                "크고 무겁고 단단한 바위입니다.")
    elif id == "Structure":
        return ("당신은 이상한 구조물을 조사한다.\n"
                "안에서 이상한 소리가 난다.\n"
                "문이 하나 보인다.\n"
                "그리고 삐 소리가 난다.")
    elif id == "StructurDoor":
        return ("문은 잠긴 듯 하다.\n"
                "둥근 구멍이 보인다. 열쇠 구멍일까?")
    elif id == "StructureDoorNoKey":
        return ("그 쪽으로 손을 내밀지만 파란 빛이 번쩍이며 닫혀 버린다.\n"
                "계획한 대로 잘 되진 않는다.")
    elif id == "StructureDoorKey":
        return ("손에 쥔 열쇠를 바라봅니다.\n"
                "이 열쇠는 열쇠 구멍과 마찬가지로 파랗게 빛납니다.")
    elif id == "BouldersKey":
        return ("가까이 다가갑니다. 저 푸른 불빛은 뭐지?\n"
                "바위틈으로 손을 뻗어 무언가를 더듬습니다.\n"
                "그것은 다름이 아니라 파랗게 빛나는 열쇠였습니다.")
    elif id == "Run":
        return ("한동안 달린다.\n"
                "저 멀리서 악마가 샷건을 들고 달려온다.\n"
                "으아아아악~~")
    elif id == "GameOver":
        return "게임오버!"
    else:
        return ""