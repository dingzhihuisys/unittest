# @dingzhihui   
# 2021/2/22   
# 2:06 下午   
# PyCharm

import unittest


# 前置  后置  运行测试
class IntegerArithmeticTestCase(unittest.TestCase):
    def setUp(self):
        pass
        # 如果没有可以不写或者pass代替

    def tearDown(self):
        pass

    def testSubtract(self):  # test method names begin with 'test'
        result = 6 - 5  # 实际结果
        hope = 1  # 期望结果
        self.assertEqual(result, hope)

    def testDivide(self):
        result = 7 / 2  # 实际结果
        hope = 3.5  # 期望结果
        self.assertEqual(result, hope)


if __name__ == '__main__':
    unittest.main()
