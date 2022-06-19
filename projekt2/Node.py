#utworzenie klasy Node ktorej 'pola' posłuza jako wskaźniki
#Self służy do reprezentowania instancji klasy. Za pomocą tego słowa kluczowego można uzyskać dostęp do atrybutów i metod klasy. Wiąże atrybuty z podanymi argumentami.

class node:
    def __init__(self, char, freq, left=None, right=None):

        # Znak
        self.char = char

        # Częstość wystąpień
        self.freq = freq

        # Gałąź lewa drzewa
        self.left = left

        # Gałąź prawa drzewa
        self.right = right

        # Lewy czy prawy - kopiec
        self.travers = ''