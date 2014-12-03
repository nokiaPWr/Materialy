class A(object):
    def __init__(self, wartosc_losowa):
        print('init A')
        self.wartosc_losowa = wartosc_losowa

    def printuj(self):
        print('printuje z A')



class B(A):
    def __init__(self):
        print('init B')
        super().__init__(5)

    def printuj(self):
        print('printuje z B')
        super().printuj()

objekt_b = B()
objekt_b.printuj()
