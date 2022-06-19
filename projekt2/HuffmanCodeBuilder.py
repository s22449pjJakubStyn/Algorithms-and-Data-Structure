# tworzy kod binarny naszego tekstu na podstawie logiki i algorytmu kodów Huffmana

import HeapSort
import Sorter
import Node

node = Node.node

binDictList = []


# travers to proces, który odwiedza wszystkie węzły drzewa i może również drukować ich wartości a Node'y to wskaźniki

def returnPath(node, travers=''):
    newTravers = travers + str(node.travers)

    if (node.left):
        returnPath(node.left, newTravers)

    if (node.right):
        returnPath(node.right, newTravers)

    if (not node.left and not node.right):
        dictElement = [node.char, newTravers]
        binDictList.append(dictElement)
    return binDictList


def returnNodes(srcText):
    sortedFreq = Sorter.sortFreqArray(srcText)

    nodes = []

    for x in range(len(sortedFreq)):
        nodes.append(node(sortedFreq[x][0], sortedFreq[x][1]))

    while len(nodes) > 1:
        # Dwa node'y o najniższym atrybucie Freq
        left = nodes[0]
        right = nodes[1]

        # Przypisanie wartości 0 lub jeden odpowiednio dla lewej i prawej gałęzi
        left.travers = 0
        right.travers = 1

        # Scalenie node'ów w jeden - konkatenacja znaków oraz sumowanie wartości Freq
        # Przypisanie obu node'ów początkowych jako potomkowie

        newChar = left.char + right.char
        newFreq = left.freq + right.freq
        newNode = node(newChar, newFreq, left, right)

        # Usunięcie dwóch małych node'ów
        # W ich miejsce wstawienie nowego node'u (rodzica)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

        # Przekopcowanie całości
        HeapSort.heapSortNd(nodes)

    return nodes[0]

    # print(returnPath(nodes[0]))
    # print(sortedFreq)
