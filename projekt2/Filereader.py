# odczytywanie z pliku z prostą instrukcja try w razie nieistnienie pliku bądź jakiś kłopotów z odczytem

from typing import final

try:
    def reader(fname):
        # Otwarcie pliku, wpisanie znaków do listy i zamknięcie
        fname = open(fname, "r")
        fileSrcText = fname.read()
        fname.close()
        return fileSrcText


except FileNotFoundError as error:
    print("File is not available:", type(error))
except Exception as error:
    print("Something went wrong:", type(error))