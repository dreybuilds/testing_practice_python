import unittest

from sys import platform


class TestDemo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1+1, 2)

    @unittest.skipIf(platform.startswith("win"), "Do not run on Windows")
    def test_case_2(self):
        self.assertIsNotNone([])