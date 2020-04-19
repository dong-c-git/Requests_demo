#coding:utf-8
import yaml
import os
#获取当前脚本所在路径
curpath = os.path.dirname(os.path.realpath(__file__))
#获取yaml文件所在路径
yamlpath = os.path.join(curpath,"cfgyaml.yaml")
#open方法直接读取出来
f = open(yamlpath,"r",encoding="utf-8")
cfg = f.read()
print(type(cfg))
print(cfg)

d = yaml.load(cfg)   #用load方法转字典
print(d)
print(type(d))
