gameWord = "apple"
guessedLetters = ['a', 'e']
maskChar = "_"

#빈 문자열로 시작하기
displayWord = ""
#한 문자씩 반복하기
for letter in gameWord:
    print(letter)
    #추측한 문자가 맞나?
    if letter in guessedLetters:
        print("맞앗쓰")
        displayWord += letter
    else:
        print("틀렸쓰")
        displayWord += maskChar
    print("displayWord는", displayWord, "입니다.")
#결과 단어 출력하기
print("원래 단어: ", gameWord)
print("마스킹한 단어: ", displayWord)