gameWord = "apple"
guessedLetters = []
maskChar = "_"

#빈 문자열로 시작하기
displayWord = ""
#한 문자씩 반복하기
for letter in gameWord:
    #추측한 문자가 맞나?
    if letter in guessedLetters:
        displayWord += letter
    else:
        displayWord += maskChar
#결과 단어 출력하기
print("원래 단어: ", gameWord)
print("마스킹한 단어: ", displayWord)