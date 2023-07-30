
def reverse_words(words):
    strippedWords= words.strip()
    wordList = strippedWords.split(" ")
    print(wordList)
    cleanedWord = [ word for word in wordList if word != ""]
    print(cleanedWord)
    wordList.reverse()
    return " ".join(wordList)



res = reverse_words("       hello    world       ")
print (f'{res}')
