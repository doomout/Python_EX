from colorama import Fore

inv = {
    "StructureKey" : False,
    "Coins" : 0
}

#인벤토리에 열쇠 추가하기
def takeStructureKey():
    inv["StructureKey"] = True

#인벤토리에 열쇠 없애기
def dropStructureKey():
    inv["StructureKey"] = False

#플레이어는 열쇠를 가졌는가?
def hasStructureKey():
    return inv["StructureKey"]

#동전을 인벤토리에 추가하기
def takeCoins(coins):
    inv["Coins"] += coins

#인벤토리에서 동선 없애기
def dropCoins(coins):
    inv["Coins"] -= coins

#플레이어가 가진 동전은 몇 개인가요?
def numCoins():
    return inv["Coins"]

#인벤토리 출력하기
def display():
    print(Fore.CYAN+"*****인벤토리*****")
    print(Fore.CYAN+"가진 동전은 ",numCoins(), "개입니다.")
    if hasStructureKey():
        print(Fore.CYAN+"파랑게 빛나는 열쇠가 있습니다.")
    print(Fore.CYAN+"****************")