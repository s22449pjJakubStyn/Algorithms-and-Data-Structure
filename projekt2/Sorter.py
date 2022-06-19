#prosty Sorter ktory zlicza ilość znaków tablicy częstotliwości wykorzystująć program FreqCounter i kopcujący tablicę

import FreqCounter
import HeapSort


def sortFreqArray(text):
    freqArray = FreqCounter.countCharacters(text)
    sortedFreqArray = HeapSort.heapSort(freqArray)

    return sortedFreqArray
