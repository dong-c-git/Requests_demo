#coding:utf-8
import xlrd
class ExcelUtil():
    def __init__(self,excelPath,sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        print("self.table>>>",self.table)
        #获取第一行作为key值
        self.keys = self.table.row_values(0)
        print("self.keys>>>",self.keys)
        #获取总行数
        self.rowNum= self.table.nrows
        print("self.rowNum>>>",self.rowNum)
        #获取总列数
        self.colNum = self.table.ncols
        print("self.colNum>>>",self.colNum)

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                #从第二行取对应values值
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

if __name__=="__main__":
    filepath = "debug_api.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())

