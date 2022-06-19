# funkcja ktora wyciaga długości tekstu i słownika i odpowiednio w pętli tworzy dwuelementową tablice

def compressText(text, dict):

    textList = list(text)

    lenTextList = len(textList)
    lenDictionary = len(dict)
    i = 0
    while i < lenTextList:
        j = 0
        while j < lenDictionary:
            if textList[i] == dict[j][0]:
                textList[i] = dict[j][1]
            j = j + 1
        i = i + 1

    return textList