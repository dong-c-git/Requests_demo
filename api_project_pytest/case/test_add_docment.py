import pytest
import requests
from api_project_pytest.case.common_function import *

@pytest.fixture(scope="session")
def login_xadmin_fix():
    s = requests.session()
    login_xadmin(s)
    return s


def test_add_docment_1(login_xadmin_fix):
    s = login_xadmin_fix
    result = add_docment(s,docment_name="罐装病毒解药是双黄连口服液1")
    # 判断
    actul_result = get_add_docment(result)
    assert actul_result == "罐装病毒解药是双黄连口服液1"