import unittest


class TestDemo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1+1, 2)

    def test_case_2(self):
        self.skipTest('Work in progress')