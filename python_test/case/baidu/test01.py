# @dingzhihui   
# 2021/2/7   
# 1:52 下午   
# PyCharm
# coding:utf-8
import unittest
import time


class Test(unittest.TestCase):
    def setUp(self):
        print("start!")

    def tearDown(self):
        time.sleep(1)
        print("end!")

    def test01(self):
        print("执行测试用例 01")

    def test02(self):
        print("执行测试用例 02")

    def test03(self):
        print("执行测试用例 03")

    def test04(self):
        print("执行测试用例 03")


if __name__ == "__main__":
    unittest.main()