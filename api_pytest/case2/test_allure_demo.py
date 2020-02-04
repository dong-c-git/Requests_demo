import pytest
import allure

@allure.step("用例的操作必要条件：带口罩")
def step1():
    print("操作必要条件：用户带n95防护口罩防护病毒")

@allure.step("用例操作必要条件：带眼罩")
def step2():
    print("操作必要条件：用户佩戴眼罩，防护病毒")

@allure.feature("冠状病毒防控")
class TestPerson():
    '''接口名称的描述'''
    @allure.story("冠状病毒防控-戴口罩，勤洗手，增加通风，注意防护")
    def test_case_1(self, login):
        '''
        用例详情的描述：接口地址：http://www.world.cn:8080/bestperson/bestall
        请求方式：post
        使用身份证申请一个key如：AppKey：cde5e16435cd0217f505a88898b60707
        :param login: 前置条件-持有身份证的人
        :return:
        '''
        step1()
        step2()
        print("测试用例1")
        assert 1==1


    @allure.story("冠状病毒防控-不带口罩")
    def test_case_2(self,login):
        print("清空用户所有操作，the person will deal!")


    @allure.story("状病毒防控-错误的戴口罩方式")
    def test_case_3(self,login):
        print("准备icu病房，the person will ill")