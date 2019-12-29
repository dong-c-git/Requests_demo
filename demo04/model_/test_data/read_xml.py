#coding:utf-8
'''
xml文件有标签：<biaoqian></biaoqian>
<shuxing abc="123">
<dui >text</dui>
<father>
    test
</father>
xml文件标签成对出现
'''
#xml文件的读取
from xml.dom import minidom
#打开xml文档
dom = minidom.parse('info.xml')
#得到文档元素对象
root = dom.documentElement

#定位文档中对象
tagname = root.getElementsByTagName("maxid")
#打印标签名称
print(tagname[0].tagName)
#获取标签对一个属性
print(tagname[0].getAttribute("username"))
#text信息
print(tagname[0].firstChild.data)

