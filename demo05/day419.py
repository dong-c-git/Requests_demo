#conding:utf-8
import pytest


@pytest.mark.parametrize("test_input,expected",
                         [("3+5",8),
                          ("2+4",6),
                          ("6+9",15),
                          ])
def test_eval(test_input,expected):
    assert eval(test_input) == expected


#参数化
test_data = [('M',{"message":"update some data!","code":0}),('F',{"message":"update some data!","code":0}),]

@pytest.mark.parametrize("test_input,expect",test_data)
def test_update(test_input,expect):
    print("输出的test_input：%s"%test_input,"对应的expect是：%s"%expect)


if __name__ == "__main__":
    pytest.main(['-s','day419.py'])