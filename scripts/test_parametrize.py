"""
test_parametrize.py

pytest中的参数化
1.使用方法
    parametirze(argnames,argvalues)
        argnames:参数名
        argvalues:参数值   数据类型为list

2.使用方式
    当测试用例只需要一个参数时
    @pytest.mark.parametrize(参数名,[参数值1,参数值2])
    参数名称必须和测试用例参数名一致,参数名:数据格式字符串
    当测试用例中需要多个参数时
    @pytest.mark.parametrize(argnames,argvalues)
    argnames:"参数1,参数2..."
    argvalues:[[参数1值,参数2值],[参数1值,参数2值],[参数1值,参数2值]...]
"""
import pytest
from common.operation_data import OperationFlie

# @pytest.mark.parametrize("phone_num", ["13800138000", "13800138001"])
# def test_verifycode(phone_num):
#     print("输入的手机号码为:", phone_num)


data = OperationFlie("register_data.csv").get_data_to_list()
print(data)


@pytest.mark.parametrize("phone,code", data)
def test_login(phone, code):
    print("手机号%s,验证码%s" % (phone, code))
