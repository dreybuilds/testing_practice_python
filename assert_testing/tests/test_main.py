import unittest

from testing_assert.main import add,subtract


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_negative(self):
        self.assertEqual(subtract(-1, 2), -3)

    def test_add_floats(self):
        self.assertEqual(add(1.1, 2.2), 3.3)
    
    def test_add_almost(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3)
