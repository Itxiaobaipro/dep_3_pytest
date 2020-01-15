"""
编写测试登录的用例
pytest中,用例的执行顺序是按照从上到下的顺序执行
使用pytest-ordering控制用例执行顺序
安装pytest-ordering
    pip install pytest-ordering
使用pytest-ordering
    在测试用例前添加
    @pytest.mark.run(order=数字)

"""
import pytest


@pytest.mark.run(order=2)
def test_add_cart():
    print("添加商品到购物车")


@pytest.mark.run(order=1)
def test_login():
    print("执行登录测试用例")


@pytest.mark.run(order=3)
def test_order():
    print("下单用例")
