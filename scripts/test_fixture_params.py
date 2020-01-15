"""
1.学习目标
   掌握pytest中带参数的fixture写法和使用
2.概念

3.语法
    @pytest.fixture(params=[列表类型])
    def 名称(request):
        函数步骤
        登录--->用户名(request.param)
        return request.param
4.需求

"""

# @pytest.fixture(params=[1, 2, 3])
# def new_data(request):
#     return request.param
#
# def test_data(new_data):
#     print("测试步骤")
#     assert new_data == 3


def test_add_cart(login):
    print("添加购物车")
