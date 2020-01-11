#coding:utf-8
import pymysql
'''
作业24：
1.使用python连mysql数据库
2.往数据库里面插入一条数据
'''
def main():
    conn = pymysql.connect(host='localhost',port=3306,database='test01',user='root',password='root',charset="utf8")
    cs1 = conn.cursor()
    #执行插入语句
    count = cs1.execute('''insert into students values(16,"上海悠悠-01",30,170,"女",5,"");''')
    count_select = cs1.execute("select * from students;")
    #循环方式每次取一条数据：
    for i in range(count_select):     #每行数据是一个元祖
        #获取查询结果
        result = cs1.fetchone()
        #打印查询结果
        print(result)
    #一次取多条数据
    result = cs1.fetchall()   #结果为一个大元祖
    print(result)
    print(count)
    conn.commit()
    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()