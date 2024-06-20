import unittest


def setUpModule():
    print('Running setUpModule')


def tearDownModule():
    print('Running tearDownModule')


class TestMyModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Running setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('Running tearDownClass')

    def setUp(self):
        print('')
        print('Running setUp')

    def tearDown(self):
        print('Running tearDown')

    def test_case_1(self):
        print('Running test_case_1')
        self.assertEqual(5+5, 10)

    def test_case_2(self):
        print('Running test_case_2')
        self.assertEqual(1+1, 2)