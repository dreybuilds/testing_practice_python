import unittest

from square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)
    
    def test_area1(self):
        square = Square(5)
        area = square.area()
        self.assertEqual(area, 25)    



