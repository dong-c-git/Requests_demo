import asyncio
from pyppeteer import launch
import random
import time
import requests
import json
import time


class TrickUrlSession(requests.Session):
    '''重写url禁止url进行urlcode'''

    def setUrl(self, url):
        self._trickUrl = url

    def send(self, request, **kwargs):
        if self._trickUrl:
            request.url = self._trickUrl
        return requests.Session.send(self, request, **kwargs)


def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


def input_time_random():
    return random.randint(100, 151)


async def try_validation(page, distance=308):
    # 将距离拆分成两段，模拟正常人的行为
    distance1 = distance - 10
    distance2 = 10
    btn_position = await page.evaluate('''
        () =>{
        return {
        x: document.querySelector('#nc_1_n1z').getBoundingClientRect().x,
        y: document.querySelector('#nc_1_n1z').getBoundingClientRect().y,
        width: document.querySelector('#nc_1_n1z').getBoundingClientRect().width,
        height: document.querySelector('#nc_1_n1z').getBoundingClientRect().height
        }}
        ''')
    x = btn_position['x'] + btn_position['width'] / 2
    y = btn_position['y'] + btn_position['height'] / 2
    await page.mouse.move(x, y)
    await page.mouse.down()
    await page.mouse.move(x + distance1, y, {'steps': 30})
    await page.waitFor(800)
    await page.mouse.move(x + distance1 + distance2, y, {'steps': 20})
    await page.waitFor(800)
    await page.mouse.up()


# 获取token主函数
async def token_main(username,password):
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://icloud.sensetime.com/senserealty/login')
    width, height = screen_size()
    # 最大化窗口
    await page.setViewport(viewport={'width': width, 'height': height})
    # 设置浏览器
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                            ' Chrome/74.0.3729.169 Safari/537.36')
    # 防止被识别，将webdriver设置为false
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    # 登录的用户名和密码
    await page.type('#BX_Layer2 > div > form > div > div > div > input',username, {'delay': input_time_random() - 50})
    await page.type('.BX_Sprite2 .el-form .el-form-item:nth-child(2) .el-form-item__content .el-input__inner',
                    password, {'delay': input_time_random()})
    # 登录时的验证
    normal_login = await page.xpath('//*[@id="BX_Layer2"]/div/form/div[4]/button')
    await normal_login[0].click()
    time.sleep(1)
    # 滑动验证
    await page.waitFor(1000)
    await try_validation(page)
    await page.waitFor(2000)
    # await shibieguanli(page)
    await page.waitFor(1000)
    # await qudaofengkong(page)
    await page.waitFor(2000)
    res = await page.cookies()
    login_token = await page.evaluate("window.localStorage.getItem('Sense-Token')", force_expr=True)
    login_companyid = await page.evaluate("window.localStorage.getItem('Sense-CompanyId')", force_expr=True)
    print("获取登录到的token是:", login_token, "获取登录后用户company:", login_companyid)
    # 图片保存
    await page.screenshot({'path': 'shibieguanli.png'})
    await page.close()
    return login_token, login_companyid


# 进入识别管理--第一版页面截图
async def shibieguanli(page):
    shibieinfo = await page.xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div/li[3]/div/span')
    await shibieinfo[0].click()


# 渠道风控--第一版页面截图
async def qudaofengkong(page):
    risk_contorl = await page.xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[1]/li/span')
    await risk_contorl[0].click()


class shujutest():

    def __init__(self,username,password):
        self.login_token, self.login_companyid = asyncio.get_event_loop().run_until_complete(token_main(username,password))
        time.sleep(5)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
            "token": eval(self.login_token),
            "Referer": "https://icloud.sensetime.com/senserealty/store/operate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Pragma": "no-cache",
            "Host": "icloud.sensetime.com",
            "Accept": "application/json, text/plain, */*"
        }

    # 案场列表获取案场名称
    async def store_find(self):
        url = 'https://icloud.sensetime.com/senserealty/store/api/sensego/console/v1.0/store/all'
        querystring = {"company_id": self.login_companyid}
        res = requests.session()
        store_name = res.get(url=url, headers=self.headers, params=querystring)
        res = store_name.json()
        store_list = res.get('list')
        for i in range(len(store_list)):
            #print(store_list[i])
            store_dict = store_list[i]
            print(store_dict['store_id'], store_dict['store_name'])


    # 渠道页面
    async def qudao_page(self,store_id):
        url = 'https://icloud.sensetime.com/senserealty/recognition/api/sensego/console/v1.0/trade'
        querystring = {"type": "0", "store_id":store_id}
        res = requests.session()
        store_name = res.get(url=url, headers=self.headers, params=querystring)
        res = store_name.json()
        store_list = res.get('list')
        if store_list:
            for i in range(len(store_list)):
                print(store_list[i])
                store_dict = store_list[i]
                #案场功能渠道风控列表
                print(store_dict['name'], store_dict['id_number'])
                #请求详细记录数据

        else:
            # 写入渠道风控风控返回数据
            return store_list


    # 渠道风控详细记录获取
    async def qudao_detail(self,id_number,store_id):
        url = 'https://icloud.sensetime.com/senserealty/recognition/customer-detail/risk/' + 'cdb978497a' + '/api/sensego/console/v1.0/trade/trace'
        querystring = {"id_number":id_number, "store_id":store_id}
        res = requests.session()
        store_name = res.get(url=url, headers=self.headers, params=querystring)
        res = store_name.json()
        store_list = res.get('list')
        print("渠道风控", store_list)
        for i in range(len(store_list)):
            # print(store_list[i])
            store_dict = store_list[i]
            # 返回案场渠道风控匹配记录数据
            print(store_dict['person_id'], store_dict['arrived_at'], store_dict['arrived_image_url'], store_dict['trace'])


# 自主报备页面数据
async def baobei_page():
    # gettoken = await page.evaluate("window.localStorage.getItem('Sense-Token')", force_expr=True)
    # getcompanyid = await page.evaluate("window.localStorage.getItem('Sense-CompanyId')", force_expr=True)
    url = 'https://icloud.sensetime.com/senserealty/recognition/api/sensego/console/v1.0/report/all'
    querystring = {"page_index": "1", "count": "20", "store_id": "cdb978497a"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxNTY3IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMCIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTg1MDMzNjYwfQ.kzNAirjAU6dEIdgk2oqF04bT30iIrML3GN9EImos-lM",
        "Referer": "https://icloud.sensetime.com/senserealty/store/operate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Pragma": "no-cache",
        "Host": "icloud.sensetime.com",
        "Accept": "application/json, text/plain, */*"
        }
    res = requests.session()
    store_name = res.get(url=url, headers=headers, params=querystring)
    res = store_name.json()
    store_list = res.get('list')
    for i in range(len(store_list)):
        # print(store_list[i])
        store_dict = store_list[i]
        # 返回自主报备页面数据
        print(store_dict['_id'], store_dict['image'])


# 报备详细记录查询数据
async def baobei_detail():
    # gettoken = await page.evaluate("window.localStorage.getItem('Sense-Token')", force_expr=True)
    # getcompanyid = await page.evaluate("window.localStorage.getItem('Sense-CompanyId')", force_expr=True)
    # url = 'https://icloud.sensetime.com/senserealty/recognition/api/sensego/console/v1.0/trade'
    url = 'https://icloud.sensetime.com/senserealty/recognition/customer-detail/report/' + 'cdb978497a' + '/api/sensego/console/v1.0/report'
    querystring = {"store_id": "cdb978497a", "_id": "5e70b77a789c5050ae850413"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxNTY3IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMCIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTg1MDMzNjYwfQ.kzNAirjAU6dEIdgk2oqF04bT30iIrML3GN9EImos-lM",
        "Referer": "https://icloud.sensetime.com/senserealty/store/operate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Pragma": "no-cache",
        "Host": "icloud.sensetime.com",
        "Accept": "application/json, text/plain, */*"
        }
    res = requests.session()
    store_name = res.get(url=url, headers=headers, params=querystring)
    res = store_name.json()
    store_list = res.get('results')
    print(store_list)
    # 渠道风控详情返回数据


# 以图搜图接口
async def search_page():
    # gettoken = await page.evaluate("window.localStorage.getItem('Sense-Token')", force_expr=True)
    # getcompanyid = await page.evaluate("window.localStorage.getItem('Sense-CompanyId')", force_expr=True)
    url = 'https://icloud.sensetime.com/senserealty/recognition/api/sensego/console/v1.0/realestate/trace'
    data = {"group_id": "1812354c64",
            "face_image": "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"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxNTY3IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMCIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTg1MDMzNjYwfQ.kzNAirjAU6dEIdgk2oqF04bT30iIrML3GN9EImos-lM",
        "Referer": "https://icloud.sensetime.com/senserealty/store/operate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Pragma": "no-cache",
        "Host": "icloud.sensetime.com",
        "Accept": "application/json, text/plain, */*"
        }
    res = requests.session()
    store_name = res.post(url=url, headers=headers, data=json.dumps(data))
    res = store_name.json()
    print("以图搜图页面", res)
    store_list = res.get('results')
    print("以图搜图页面", store_list)
    for i in range(len(store_list)):
        # print(store_list[i])
        store_dict = store_list[i]
        # 返回案场渠道风控匹配记录数据
        print(store_dict['person_id'], store_dict['arrived_at'], store_dict['arrived_image_url'], store_dict['trace'])


# 到访统计-总数
async def daofang_page_count():
    # gettoken = await page.evaluate("window.localStorage.getItem('Sense-Token')", force_expr=True)
    # getcompanyid = await page.evaluate("window.localStorage.getItem('Sense-CompanyId')", force_expr=True)
    url = 'https://icloud.sensetime.com/senserealty/recognition/api/sensego/console/v1.0/peoplecount/summary'
    data = {"store_id": "cdb978497a", "end_time": "158487500", "start_time": "1582992000", "ask_id": "2"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxNTY3IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMCIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTg1MDMzNjYwfQ.kzNAirjAU6dEIdgk2oqF04bT30iIrML3GN9EImos-lM",
        "Referer": "https://icloud.sensetime.com/senserealty/store/operate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Pragma": "no-cache",
        "Host": "icloud.sensetime.com",
        "Accept": "application/json, text/plain, */*"
        }
    res = requests.session()
    store_name = res.post(url=url, headers=headers, data=json.dumps(data))
    res = store_name.json()
    print("到访统计页面", res)
    person_count = res.get('capture_count')
    first_time_count = res.get('first_time_count')
    print("到访统计人数", person_count, "首次到访统计数据", first_time_count)


# 到访统计-访客明细
async def daofang_page_summary():
    # gettoken = await page.evaluate("window.localStorage.getItem('Sense-Token')", force_expr=True)
    # getcompanyid = await page.evaluate("window.localStorage.getItem('Sense-CompanyId')", force_expr=True)
    url = 'https://icloud.sensetime.com/senserealty/recognition/api/sensego/console/v1.0/peoplecount/total'
    data = {"store_id": "cdb978497a"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxNTY3IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMCIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTg1MDMzNjYwfQ.kzNAirjAU6dEIdgk2oqF04bT30iIrML3GN9EImos-lM",
        "Referer": "https://icloud.sensetime.com/senserealty/store/operate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Pragma": "no-cache",
        "Host": "icloud.sensetime.com",
        "Accept": "application/json, text/plain, */*"
        }
    res = requests.session()
    store_name = res.post(url=url, headers=headers, data=json.dumps(data))
    res = store_name.json()
    print("到访统计人数页面", res)
    people_count = res.get('people_count')
    print("到访统计人数数据", people_count)


# 识别结果
async def shibie_detail():
    # gettoken = await page.evaluate("window.localStorage.getItem('Sense-Token')", force_expr=True)
    # getcompanyid = await page.evaluate("window.localStorage.getItem('Sense-CompanyId')", force_expr=True)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxNTY3IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMCIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTg1MDMzNjYwfQ.kzNAirjAU6dEIdgk2oqF04bT30iIrML3GN9EImos-lM",
        "Referer": "https://icloud.sensetime.com/senserealty/store/operate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Pragma": "no-cache",
        "Host": "icloud.sensetime.com",
        "Accept": "application/json, text/plain, */*"
        }
    res = requests.session()
    # 先查设备id
    url = 'https://icloud.sensetime.com/senserealty/recognition/api/sensego/console/v1.0/group/storedevice'
    querystring = {"store_id": "cdb978497a"}
    store_devicemap = res.get(url=url, headers=headers, params=querystring)
    devicemap = store_devicemap.json()
    store_map_list = devicemap.get('group_device_map')
    store_device = store_map_list.get('cdb978497a')
    print(store_device)
    # 识别结果查询
    start_time = "1584806400"
    end_time = "1584875885"
    group_id = "cdb978497a"
    device_id = "00:0c:29:b2:05:77"
    limit = 1000
    geturl = "https://icloud.sensetime.com/senserealty/recognition/api/sensego/console/v1.0/datacenter/visitinfo/query/device?start_time=%s&end_time=%s&group_id=%s&device_id=%s&limit=%s" % (
    start_time, end_time, group_id, device_id, limit)
    print(geturl)
    Trick = TrickUrlSession()
    Trick.setUrl(geturl)
    getrequest = Trick.get(url=geturl, headers=headers)
    print(getrequest.json())


# 主函数
async def main():
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://icloud.sensetime.com/senserealty/login')
    width, height = screen_size()
    print("获取屏幕长的值和类型", width, type(width))
    # 最大化窗口
    # await page.setViewport({width:width,height:height})
    await page.setViewport(viewport={'width': width, 'height': height})
    # 设置浏览器
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                            ' Chrome/74.0.3729.169 Safari/537.36')
    # 防止被识别，将webdriver设置为false
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    # 登录的用户名和密码
    await page.type('#BX_Layer2 > div > form > div > div > div > input', 'SKtest', {'delay': input_time_random() - 50})
    await page.type('.BX_Sprite2 .el-form .el-form-item:nth-child(2) .el-form-item__content .el-input__inner',
                    'SKtest123', {'delay': input_time_random()})
    # 登录时的验证
    normal_login = await page.xpath('//*[@id="BX_Layer2"]/div/form/div[4]/button')
    await normal_login[0].click()
    time.sleep(1)
    # 滑动验证
    await page.waitFor(1000)
    await try_validation(page)
    await page.waitFor(2000)
    await shibieguanli(page)
    await page.waitFor(1000)
    await qudaofengkong(page)
    await page.waitFor(2000)
    res = await page.cookies()
    content = await page.evaluate("window.localStorage.getItem('Sense-Token')", force_expr=True)
    print(res)
    print(page.url)
    print(content)
    # 图片保存
    await page.screenshot({'path': 'shibieguanli.png'})
    await page.close()


if __name__ == "__main__":
    # asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().run_until_complete(store_find())
    asyncio.get_event_loop().run_until_complete(qudao_page())
    asyncio.get_event_loop().run_until_complete(qudao_detail())
    asyncio.get_event_loop().run_until_complete(baobei_page())
    asyncio.get_event_loop().run_until_complete(baobei_detail())
    asyncio.get_event_loop().run_until_complete(search_page())
    asyncio.get_event_loop().run_until_complete(daofang_page_count())
    asyncio.get_event_loop().run_until_complete(daofang_page_summary())
    asyncio.get_event_loop().run_until_complete(shibie_detail())
    # asyncio.get_event_loop().run_until_complete(shibie_detail())