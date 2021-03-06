class Duck(object):
    def __init__(self, name):
        self.name = name

    def quack(self, how_many=1):
        #print('{}: {}'.format(self.name, ' '.join(['Quack!']*how_many)))
        print('{}: {}'.format(self.name, 'Quack! '*how_many))

    def __call__(self, how_many=1):
        self.quack(how_many)



class DuckHerd(object):
    def __init__(self, *args):
        self.ducks = []
        self.ducks.extend(args)

    def __len__(self):
        return len(self.ducks)

    def __iadd__(self, duck):
        self.ducks.append(duck)
        return self

kaczka1 = Duck('Tomek')
kaczka2 = Duck('Leszek')
dh = DuckHerd(kaczka1, kaczka2)
dh+=Duck('Witold')
print(len(dh))
