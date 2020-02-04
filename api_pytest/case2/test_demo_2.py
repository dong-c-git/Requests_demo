import pytest
import allure


@allure.step("用例的操作必要条件：普通洗手")
def step1():
    print("用例的操作必要条件：普通洗手")

@allure.step("用例的操作必要条件：使用洗手液洗手")
def step2():
    print("用例的操作必要条件：使用洗手液洗手")

@allure.feature("冠状病毒防控-第二步")
class TestPerson2():
    '''接口名称的描述'''
    @allure.story("冠状病毒防控-第二步：勤洗手，增加通风，注意防护")
    def test_case_1(self, login):
        '''
        用例详情的描述：接口地址：http://www.world.cn:8080/bestperson/bestalll
        请求方式：get
        使用身份证申请一个key如：AppKey：cde5e16435cd0217f505a88898b60707
        :param login: 前置条件-持有身份证
        :return:
        '''
        step1()
        step2()
        print("测试用例2")
        assert 1==1


    @allure.story("冠状病毒防控-第二步：忘了洗手")
    def test_case_2(self,login):
        print("清空用户所有操作，the person will deal!")


    @allure.story("冠状病毒防控-第二步：添加84洗手液")
    def test_case_3(self,login):
        print("84洗手液有效清楚细菌")

