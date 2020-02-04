#coding:utf-8
import requests
from api_project_pytest.case.common_function import login_xadmin
import os
import pytest

def pytest_addoption(parser):
    parser.addoption(
                     "--cmdhost",
                     action = "store",
                     default = "http://49.235.92.12:8020",
                     help = "test case project host address"
                    )


@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''获取命令行参数'''
    # 获取命令行参数给到环境变量
    os.environ["xadmin_host"] = request.config.getoption("--cmdhost")
    print("当前用例运行测试环境:%s"%os.environ["xadmin_host"])

@pytest.fixture(scope="session")
def login_xadmin_fix(request):
    s = requests.session()
    login_xadmin(s)
    def close_s(): #关闭session
        s.close()
    request.addfinalizer(close_s)  #终结
    return s



