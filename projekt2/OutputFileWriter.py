# program do zapisu słownika i kodu binarnego do pliku

import HuffmanCodeBuilder
import Converter
import Filereader

# def toBinary(a):
#   l,m=[],[]
#   for i in a:
#     l.append(ord(i))
#   for i in l:
#     m.append(int(bin(i)[2:]))
#   return m

def writeDictionary(fileIn, fileOut):
    with open(fileOut, "w") as fout:
        srcText = Filereader.reader(fileIn)
        dictionary = HuffmanCodeBuilder.returnPath(
            HuffmanCodeBuilder.returnNodes(srcText))

        dictElement = ''
        dictFull = ''
        x = 0
        while x < len(dictionary):
            char = dictionary[x][0]
            freq = dictionary[x][1]
            dictElement = char + ": " + freq + "\n"
            dictFull = dictFull + dictElement
            x = x + 1
            # byte = (dictFull.encode())

        fout.write(dictFull)
        fout.close()

    return dictionary


def writeResult(fileIn, fileOut):
    dictionary = writeDictionary(fileIn, fileOut)

    srcText = Filereader.reader(fileIn)
    converted = Converter.compressText(srcText, dictionary)

    newConverted = ''

    i = 0
    lenConverted = len(converted)
    # byte = fileIn.encode()
    with open(fileOut, "a") as fout:
        fout.write(str('\n'))
        while i < lenConverted:
            newConverted = newConverted + converted[i]
            i = i + 1
        fout.write(str(newConverted))
        fout.close()
