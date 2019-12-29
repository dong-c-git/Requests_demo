#coding:utf-8
"""
有一个数据list of dict
a = [
    {"yoyo1":"123456"},
    {"yoyo2":"123456"},
    {"yoyo3":"123456"}
    ]
写入到txt文件，内容格式如下：
yoyo1,123456
yoyo2,123456
"""
def write_txt(list):
    if not list:
        return False
    write_ = list
    len_ = len(list)
    with open("test.txt", "a+", encoding="utf-8") as fp:
        for i in range(len_):
            write_keys = write_[i].keys()
            for j in write_keys:
                wirte_info = j+","+write_[i][j]
                fp.write(wirte_info+"\n")


if __name__ == "__main__":
    a = [{"yoyo1": "123456"},{"yoyo2": "123456"},{"yoyo3": "123456"}]
    write_txt(a)