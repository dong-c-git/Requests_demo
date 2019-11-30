1. 接口自动化测试概念：
   让程序代替人为对接口项目进行自动化验证的测试过程；
2. 实现方式：
   代码；工具；
3. 接口测试工具的不足：
      - 测试数据的不好控制；
      - 不方便测试加密接口；
      - 扩展能力不足；

4. request库：
   request库采用apache2开源协议的http库，相比urllib，request库更加丰富；

5. requets库具有get\post\put\delete\head\options请求方式；

   import requests
   response = requests.get("http://www.baidu.com")
   返回的是response对象；
   想要的请求方法和对象都在response对象中；

   请求参数：params
      方式1：params = {"id":1001}
      方式2：params = {"id":"1001,1002"}
      方式3：params = {"id":"1001","kw":"北京"}
   请求方式：
      requests.get(url=url,params=params)

6、post请求：
   作用：新增资源
   应用：导包import requests
   调用post方法requests.post()
   示例：request.post(url,json,headers)

   参数：url新增接口url地址
   json：新增请求报文
   headers：请求信息头

   响应状态：requests.status_code
   响应信息：requests.json

   data与json的区别
   data:字典对象
   json：json字符串
   提示：1、在python中字典对象和json字符串长得一样，但是后台格式是有区别的
   如何将字典对象转换为json字符串
   1、导入json
   2、json.dumps(字典对象)#转换json字符串

   响应数据json和text区别
   json()返回数据是字典类型，可以通过键名来获取响应的值
   text返回的是字符串类型，无法通过键名来获取响应数据的值

7、put方法：
   作用：更新资源
   应用：导入包
   调用put方法

   参数：和post请求参数一致

   响应response.json()
   response.status_code

8、delete方法：
   作用：删除资源
   应用：先导包
        调用delete方法
   响应：
        响应状态码：204

9、响应内容：
   response.status_code  状态码
   response.url          请求url
   response.encoding     查看响应头部字符编码
   response.headers      头信息
   response.cookies      cookie信息
   response.text         文本形式的响应内容
   response.content      字节形式的响应内容
   response.json()       json形式的响应内容

10、cookie和content
   cookie获取响应的cookie信息
   text是以文本形式解析响应内容
   content 以字节码形式解析响应内容，解析图片就是二进制图片流

11、cookie是服务器生成，作用是区分同一请求客户端
    获取：response.cookies
    可以用键名形式取出对应cookie
    设置请求的cookie时，requests.get(cookies=cookie)

12、session对象是一个非常用的对象：
    session对象可以自动保存服务器产生的cookies信息，
    并且自动在下一条请求上附件

    一次会话：客户端和服务器创建连接开始，直到客户端和服务器断开结束

13、session对象的应用：
    创建session对象：
    req = requests.session()
    应用：通过session对象发送请求
    session.get()
    session.post()
    session.delete()
    session.put()
    无论通过session对象调用那个请求方法，返回的都是一个response对象

14、集成到unittest框架：
    将接口集成到unittest框架
    结构：
    setUp:作用test开始方法执行之前会被执行
          应用获取session对象
          登录url
          验证码url

    tearDown:作用test方法执行后会被执行
          关闭session对象

    test_login_sucess:测试方法，登录成功后执行
          请求验证码让session记录cookie
          登录请求
          断言
          
    test_username_not_exist:测试方法用户名不存在
    test_password_error:测试方法，密码错误










