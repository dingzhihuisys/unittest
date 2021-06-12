# @dingzhihui   
# 2021/2/22   
# 2:29 下午   
# PyCharm
"""
Project:学习和使用unittest框架设计hq登录测试用例
"""
# 3.导入requests和unittest模块
import requests
import unittest


# 4.编写测试用例和断言
def login(passport, pwd, passport_Type):
    """账号：passport，密码：password，登录方式：passportType"""
    url = "http://eauth.downtown8.net/passport/login"
    headers = {
        "content-type": "application/json; charset=utf-8"
    }  # get方法其它加个ser-Agent就可以了
    param = {
        "passport": passport,
        "pwd": pwd,
        "passportType": passport_Type
           }
    print(param)
    res = requests.post(url, headers=headers, params=param)
    print(res.text)
    return res.json()


class Jenkins_login(unittest.TestCase):
    def test_login1(self):
        """测试登录：正确账号，正确密码"""
        passport = "758737541@qq.com",  # 正确账号，
        pwd = "DZh123456",  # 正确密码，
        passport_Type = "email",
        result = login(passport, pwd, passport_Type)
        print(result)
        self.assertEqual(200, result)


if __name__ == "__main__":
    unittest.main()
