import unittest
from cutter2 import Cutter

class TestCutter(unittest.TestCase):
    def test_spawn_object_cutter(self):
        cutter = Cutter(lines=1, characters=1)
        self.assertIsInstance(cutter, Cutter)

    @unittest.skip('Not yet implemented')
    def test_cut_input_without_cutting(self):
        cutter = Cutter(lines=5, characters=20)
        input_data = '''one
two
three
four'''
        self.assertEqual(['one', 'two', 'three', 'four'], cutter.cut(input_data))

    @unittest.skip('Not yet implemented')
    def test_cut_input_with_more_characters(self):
        cutter = Cutter(lines=5, characters=20)
        input_data = '''qwertyuiop
twotwotwotwotwotwotwotwo
threethreethreethreethree
four'''
        self.assertEqual(['qwertyuiop', 'twotwotwotwotwotwotw', 'threethreethreethree', 'four'], cutter.cut(input_data))

    @unittest.skip('Not yet implemented')
    def test_cut_less_data(self):
        cutter = Cutter(lines=2, characters=2)
        input_data = '''one
two
three
four'''
        self.assertEqual(['on', 'tw'], cutter.cut(input_data))

    @unittest.skip('Not yet implemented')
    def test_cut_more_data(self):
        cutter = Cutter(lines=2, characters=2)
        input_data = '''oneoneoneoneoneoneone
twotwotwotwotwotwotwotwo
threethreethreethreethree
four'''
        self.assertEqual(['on', 'tw'], cutter.cut(input_data))

if __name__ == "__main__":
    unittest.main()
