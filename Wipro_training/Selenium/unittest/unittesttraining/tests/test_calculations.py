import sys
import  unittest

from src.calculations import add, sub, mul, div, ne


class TestCalculations(unittest.TestCase):
    # def add(self):
    #     res = add(10,5)
    #     self.assertEqual(res, 15, msg='Addition error')
    #
    #
    # def test_sub(self):
    #     res = sub(10,5)
    #     self.assertEqual(res, 5, msg='subtraction error')
    #
    #
    # def test_mul(self):
    #     res =mul(10,5)
    #     self.assertEqual(res, 50, msg='multiplication error')

    #
    # def test_div(self):
    #     res = add(10,5)
    #     self.assertEqual(res, 2.0, msg='division error')
    @unittest.skipIf( sys.version_info < (3, 13)  , reason='Not Impl yet')
    def test_ne(self):
        res = ne(10,20)
        self.assertTrue(res , msg = 'NE')

    # def test_div(self):
    #     res = div(10, 0)
    #     self.assertRaises(ZeroDivisionError , msg='No Exception')
