import unittest
import requests


def create_employee(token, brand_id, employee_name, is_store_all, store_ids, add_email, add_mobile, get_country_code,
                    promission_role_id, employee_number, promission_role_key, pass_code):
    url = "http://posuser.downtown8.net/employee/createEmployee"
    data = {
        "brandId": brand_id,
        "employeeName": employee_name,  # 小于40个字符 任意
        "isStoreAll": is_store_all,  # 门店全选 0 , 1
        "storeIds": store_ids,
        "email": add_email,
        "mobile": add_mobile,
        "countryCode": get_country_code,
        "promissionRoleId": promission_role_id,
        "employeeNumber": employee_number,
        "promissionRoleKey": promission_role_key,
        "passcode": pass_code
    }
    headers = {"Content-Type": "application/json;charset=UTF-8", "token": token}
    print("这里是整体运行的参数-------", data)
    result_one_employee = requests.post(url, params=data, headers=headers)
    print("create_employee打印结果----------", result_one_employee.text, type(result_one_employee))
    return result_one_employee


class execute_create_employee(unittest.TestCase):
    def test_create_employee01(self):
        """创建 门店经理，并生成4位码"""
        # 门店经理权限：个人码，后台权限，需要调生成4位码接口
        token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyOSwidG9rZW5faWQiOiI5MmYwNzcxMVMxMTU2UzQ4ZjNTODdmN1MyZTEzODNjYzA4ZDkiLCJicmFuZF9pZHMiOls2MDAxMDIsNjAwMTAzLDYwMDI4OSw2MDAzMzNdLCJicmFuZF9pZCI6IjYwMDMzMyIsIm9wX2VtcGxveWVlIjo1OTAsImlhdCI6MTYxNjMzMzM3MCwiZXhwIjoxNjE2OTM4MTcwfQ.qRa3lYisoQ5crhielZuUBEjE7vCpYMu9COg_opyebyj41S-DOdbEq_0tzDEJWwy1FaOSs94mit7Y5GbDPCLlLxX2FsJgdYbrWNxsDLbTkTm6lDGZN0tB4zBP_I-P_3FJjIlu_PnDZmG_0uEW86pCSKvsVfd8E858pJ0MYPhBY5U3kPPFnkpTe07V4ce0umm0P7b7XSdqViMcHTAZdAXc1peWPxBRIMMv1jSFK7OYEcyRupan9eaZY_kQCL2nBPqsok0w5oflJm5MYiHwcnQpHU4tk-VKIwCf8N8W0Ae6krwpiLO65fmobitWLZblF7iYhY6eJy2guo3emqcQFwwfSw"
        # print("这里是token的值", token)
        brand_id = "600333"
        # print("这里是brand_id的值", brand_id)
        employee_name = "liwei"  # 随机创建一个姓名
        print("test_create_employee01----门店经理的名字叫：", employee_name)
        # print("这里是employee_name的值", employee_name)
        # 0  代表不是全选
        # 1  代表是全选    store_ids可以为空
        is_store_all = 0
        print("isStoreAll：", is_store_all)
        # store = execute_list_employee_store.test_list_employee_store01(None)[0].get("stores")[0].get("storeId")
        store_ids = [800581]
        print("test_create_employee01--门店的数量+：", len(store_ids), "storeIds:", store_ids)
        add_email = "12345598@qq.com"
        add_mobile = ""
        get_country_code = ""
        promission_role_id = 103  # 岗位id
        # print("这里是promission_role_id的值", promission_role_id)
        employee_number = ""  # 工号
        promission_role_key = "storeManager"  # 岗位value
        # print("这里是promission_role_key的值", promission_role_key)
        pass_code = "5880"
        create_store_manager = create_employee(token, brand_id, employee_name, is_store_all, store_ids, add_email,
                                               add_mobile, get_country_code, promission_role_id, employee_number,
                                               promission_role_key, pass_code)
        print("000----------------00000", create_store_manager.json())


if __name__ == '__main__':
    unittest.main()