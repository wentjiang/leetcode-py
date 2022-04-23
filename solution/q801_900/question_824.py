from functools import reduce


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowelSet = ('a', 'e', 'i', 'o', 'u')
        resultList = []
        for index, word in enumerate(sentence.split(" ")):
            if word[0].lower() in vowelSet:
                goatLatinWord = word + "ma" + (index + 1) * "a"
            else:
                goatLatinWord = word[1:] + word[0] + "ma" + (index + 1) * "a"
            resultList.append(goatLatinWord)
        return reduce(lambda word1, word2: word1 + " " + word2, resultList)
