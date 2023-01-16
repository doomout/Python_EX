pet = {
    "animal" : "Iguana",
    "name" : "Iggy",
    "food" : "Veggies",
    "mealsPerDay" : 1
}

print(pet["name"], "the",pet["animal"])
print("eats", pet["mealsPerDay"], "times a day")

#mealsPerDay를 2로 변환
pet["mealsPerDay"] = 2
print(pet["name"], "eats", pet["mealsPerDay"], "meals")

#딕셔너리를 리스트로 구현
pets = [
{
    "animal" : "Iguana",
    "name" : "Iggy",
    "food" : "Veggies",
    "mealsPerDay" : 1
},
{
    "animal" : "Goldfish",
    "name" : "Goldy",
    "food" : "Flakes",
    "mealsPerDay" : 3
}
]

for pet in pets:
    print(pet["animal"],"-", pet["name"])