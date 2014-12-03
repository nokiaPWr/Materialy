class ListPow(list):
    def append(self, item):
        try:
            super().append(item ** item)
        except:
            return False

    def sort(self):
        super().sort(reverse=True)

    def pop(self):
        super().pop(0)


l = ListPow()
l.append(1)
l.append(2)
l.append(3)
l.append('A')
l.append([1,2,3])
print(l)

l.sort()

print(l)

l.pop()

print(l)

