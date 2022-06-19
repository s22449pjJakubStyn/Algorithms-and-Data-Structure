# plik główny w którym są wywoływane pliki do oczytu i zapisu i poszczególne metody

import HuffmanCodeBuilder
import Converter
import Filereader
import OutputFileWriter

fSrcName = "tekst.txt"
fOutName = "code.txt"

srcText = Filereader.reader(fSrcName)

OutputFileWriter.writeResult(fSrcName, fOutName)