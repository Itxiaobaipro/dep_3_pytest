"""
test_xfail.py

xfail(condition,reason)
    condition:当条件为真时,期望用例执行失败;
    reason:原因

    condition      result
    True            False    原意
    True            True     不希望出现
    False           True     原意
    False           False    不希望出现

@pytest.mark.xfail(condition,reason)

x  当条件为真,用例执行失败   xfailed
X  当条件为真,用例执行成功   xpassed
F  当条件为假,用例执行失败   failed
.  当条件为假,用例执行成功   passed

在实际执行脚本的过程中,不希望出现xpassed情况,
因为xpassed属于bug,在配置文件中添加参数xfail_strict = true  将xpassed直接标记为failed
"""
import pytest


# 当条件为真,用例执行失败--希望的结果
@pytest.mark.xfail(condition=True, reason="")
def test_1():
    print("当条件为真,用例执行失败")
    assert False


# 当条件为真,用例执行成功
@pytest.mark.xfail(condition=True, reason="")
def test_2():
    print("当条件为真,用例执行成功")
    assert True


# 当条件为假,用例执行失败--希望的结果
@pytest.mark.xfail(condition=False, reason="")
def test_3():
    print("当条件为假,用例执行失败")
    assert False


# 当条件为假,用例执行成功
@pytest.mark.xfail(condition=False, reason="")
def test_4():
    print("当条件为假,用例执行成功")
    assert True
