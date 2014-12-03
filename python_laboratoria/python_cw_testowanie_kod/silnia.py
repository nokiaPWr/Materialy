def silnia_r(n):
    if n == 1:
        return n
    else:
        return n * silnia_r(n-1)


#ponizej przyklad (w osobnym pliku, modul_testowany_test.py)
import unittest
import modul_testowany

class TestyModulu(unittest.TestCase):
    def test_pierwszy_test_metody(self):
        wynik = modul_testowany.metoda_testowana(2, 2)
        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_assert_raises(self):
        self.assertRaises(TypWyjatku, modul_testowany.metoda_testowana, (argument1, argument2))
if __name__ == '__main__':
    unittest.main()
