#coding:utf-8
import pandas as pd

#pandas读excel
res = pd.read_excel("debug_api.xlsx")
#输出标题列
print(res.columns.values)
#输出第一行数据不包含表头
data = res.loc[0].values
print("对应类型是：",type(data),"数据是：",data)

#pandas写excel
write_data = {"姓名":["测试1","测试2","测试3","测试4"],"性别":["测试数据1","测试数据2","测试数据3","测试数据4"]}
df = pd.DataFrame(write_data)
writer_exe = pd.ExcelWriter(r"test1.xlsx")

df.to_excel(writer_exe,sheet_name=r"sheet1",index=False,header=True)
writer_exe.save()
