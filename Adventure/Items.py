items = [
    {
        "id":"health",
        "description": "체력 회복 물약",
        "key":"H",
        "cost":100
    },
    {
        "id":"blaster",
        "description": "광선총",
        "key":"B",
        "cost":250
    },
    {
        "id":"shield",
        "description": "우주 수류탄 3개",
        "key":"G",
        "cost":300
    },
    {
        "id":"shield",
        "description": "방패",
        "key":"S",
        "cost":500
    },
    {
        "id":"life",
        "description": "생명력 추가",
        "key":"L",
        "cost":1000
    },
]

#아이템 얻기
def getItem():
    #결과 저장 변수
    result = []
    for item in items:
        #빈 리스트 만들기
        i = []
        #이름(키) 추가하기
        i.append(item["key"])
        #description + cost 추가하기
        i.append(item["description"]+ "(" + str(item["cost"])+ ")")
        #이 아이템을 결과애 추가하기
        result.append(i)
    #결과 반환하기 (예)L, 생명력 추가(1000)
    return result