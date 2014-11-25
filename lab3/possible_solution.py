import sys

def get_st_dict(filename):
  licz={}
  try:
    with open(filename) as f:
      for losowanie in f:
        for i in losowanie.split()[-1].split(","):
          if i not in licz:
            licz[i] = 0
          licz[i] += 1
  except FileNotFoundError:
     print("Podany plik nie istnieje!")
  return licz

def display_stats(filename='stats.txt'):
  licz=get_st_dict(filename)
  wszystkie_liczby=sum(licz.values())
  for liczba,ilosc in licz.items():
    print("{} wypadlo {} razy ({}%)".format(liczba, ilosc, 100*ilosc/wszystkie_liczby))

if __name__ == '__main__':
  if len(sys.argv)>1:
    display_stats(sys.argv[1])
  else:
    display_stats()
