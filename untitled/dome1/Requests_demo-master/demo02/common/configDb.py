#coding:utf-8
import pymysql
import demo02.readConfig as readConfig
from demo02.common.log import Mylog as log

localReadConfig = readConfig.ReadConfig()

class MyDB:
    global host,username,password,port,database,config
    host = localReadConfig.get_db("host")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    database = localReadConfig.get_db("database")
    config = {
        'host':str(host),
        'user':username,
        'passwd':password,
        'port':int(port),
        'db':database
    }
    def __init__(self):
        self.log = log.get_log()
        self.logger = self.log
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            self.db = pymysql.connect(**config)
            self.cursor = self.db.cursor()
            print("connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self,sql,params):
        self.connectDB()
        self.cursor.execute(sql,params)
        self.db.commit()
        return self.cursor

    def get_all(self,cursor):
        value = cursor.fetchall()
        return value

    def get_one(sel,cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("database closed!")




