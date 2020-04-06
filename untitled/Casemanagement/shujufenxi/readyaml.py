#coding:utf-8
import yaml
import os

curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath,'config.yaml')

f = open(yamlpath,'r',encoding='utf-8')
cfg = f.read()
print(cfg)
print(type(cfg))

#解决安全警告配置形成字典
d = yaml.load(cfg,Loader=yaml.FullLoader)
yaml.warnings({'YAMLLoadWarning': False})
print(d)
print(type(d))

# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(cur_path, 'logs')
print(cur_path)
print(log_path)