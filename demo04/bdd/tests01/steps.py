#coding:utf-8
from lettuce import *
#@--python装饰器
#假如我有一个数字x 给程序去读的"注释"
#Given I have the number 0
@step('I hava the number (\d+)') #正则表达式
def hava_the_number(step,number):
    world.number = int(number)


#我计算它的阶乘
#when I compute its factorial
@step('I compute its factorial')
def compute_its_fatorial(step):
    world.number = factorial(world.number)
    #world.number 计算阶乘之后的结果

#然后，就看到了结果y,比较或测试的过程
@step('I see the number (\d+)')
def check_number(step,expected):
    expected = int(expected)
    assert world.number == expected,"Got %d"%world.number

#阶乘的计算过程
def factorial(number):
    number = int(number)
    if (number == 0) or (number==1):
        return 1
    else:
        return number*factorial(number-1)