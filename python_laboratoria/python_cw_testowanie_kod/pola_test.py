import unittest
import pola

class PolaTest(unittest.TestCase):
    def test_proste_pole_kwadratu(self):
        wynik = pola.pole_kwadratu(2)
        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)




if __name__ == "__main__":
    unittest.main()
