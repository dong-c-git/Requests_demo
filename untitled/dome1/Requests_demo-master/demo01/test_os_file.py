#coding:utf-8
"""
题目要求：
1：获取当前目录下所有文件，然后做如下处理：
1）文件名去重复。
2）选出文件大于10m的
3）获取到文件的md5值，然后利用这个md5值对文件名进行重命名（其中md5代表一个文件属性）
4）打印出最后的符合条件的所有文件名

温馨提示：
1）我们是要获取所有的文件 而不是目录
2）去重复不是删除文件，而是对重复的文件名进行重命名
3）想办法获取文件的md5值
4）最好是函数的形式实现哦
"""

import os,hashlib

allfiles = []
templist = {}
end_file = []

class GetFile:
    def __init__(self,dirpath):
        self.dirpath = dirpath

    def get_all_file(self):
        #通过os.walk获取目录下所有文件名
        for root,dirs,files in os.walk(self.dirpath):
            for file in files:
                #判断size
                size = os.path.getsize(os.path.join(root,file))
                if size >= 10485760:
                    #文件名添加到allfiles列表里
                    allfiles.append(os.path.join(root,file))
        #重命名
        for i in range(len(allfiles)):
            #如果md5在字典的key已存在
            if self.get_md5(allfiles[i]) in templist.keys():
                templist[self.get_md5(allfiles[i])+str(i)] = allfiles[i].split(".")[0] + str(i) + "." + allfiles[i].split(".")[-1]
            else:
                templist[self.get_md5(allfiles[i])] = allfiles[i]
        #最后的文件
        for file in templist.values():
            end_file.append(file)

        return end_file

    @staticmethod
    def get_md5(filename):
        f = open(filename,'rb')
        m1 = hashlib.md5()
        m1.update(f.read())
        hash_code = m1.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
        return md5

if __name__ =='__main__':
    path = r'~\Downloads'
    print(GetFile(path).get_all_file())