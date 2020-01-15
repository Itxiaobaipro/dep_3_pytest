"""
test_skip.py
pytest中跳过测试
方法:
skipif(condition,reason)
    condition:当条件为真时,跳过测试
    reason:跳过测试原因
使用:
在测试用例之前添加:
    @pytest.mark.skipif(条件,reason="跳过测试原因")
    测试用例

"""
import pytest
import random

num = random.randint(1, 10)


@pytest.mark.skipif(condition=num % 2 == 0, reason="女性跳过")
def test_browser_electronic():
    """浏览电子产品"""
    print("浏览电子产品")


@pytest.mark.skipif(condition=num % 2 == 1, reason="男性忽略")  # 跳过测试
def test_browser_maquillage():
    """浏览化妆品"""
    print("浏览化妆品")
