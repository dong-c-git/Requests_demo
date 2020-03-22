import asyncio
from pyppeteer import launch
import random
import time

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

#案场列表
async def anchangguanli(page,store_id):
    #输入案场id查询案场名称
    await page.type('.el-input .el-input--medium .el-input--suffix',store_id, {'delay': input_time_random() - 50})
    store_name = await page.xpath('//*[@id="table"]/div[3]/table/tbody/tr/td[3]/div/div/span/div[2]/span')
    return_name = await store_name[0].jsonValue()
    return return_name

#进入识别管理
async def shibieguanli(page):
    shibieinfo = await page.xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div/li[3]/div/span')

#渠道风控
async def qudaofengkong(page,store_name):
    #进入渠道风控
    risk_contorl =  await page.xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[1]/li/span')
    await risk_contorl[0].click()
    await asyncio.sleep(1)
    #点击案场名称列表，获取案场名称列表
    input_click = await page.xpath('//*[@id="CreateForm"]/div[1]/div/div/div/input')
    await input_click[0].click()
    li_list = await page.xpath('/html/body/div[4]/div[1]/div[1]/ul')
    item_list = []
    for li in li_list:
        #依次点击每个案场名称
        a = await li.xpath('.//div[@class="el-select-dropdown__item"]/span')
        await a[0].click()
        await asyncio.sleep(1)
        #先截图保存
        await li.screenshot({'path': '渠道风控.png'})
        #定位人员渠道列表
        try:
            personqudao = await page.xpath('//*[@id="table"]/div[3]/table/tbody/tr')
            xiangqing = await personqudao[0].xpath('//*[@id="table"]/div[4]/div[2]/table/tbody/tr[1]/td[15]/div/button[1]/span')
            await xiangqing[0].click()
            await xiangqing[0].screenshot({'path': '人员渠道风控.png'})
        except Exception as e:
            pass


#自主报备
async def adjust(page):
    #进入自主报备
    adjust = await page.xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[2]/li/span')
    await adjust[0].click()
    #输入案场名称

    #截图保存


#以图搜图
async def searchpic(page):
    #进入以图搜图
    searchpicinfo = await page.xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[2]/li/span')
    await searchpicinfo[0].click()
    #输入案场名称


#到访统计
async def daofangcount(page):
    daofanginfo = await page.xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[4]/li/span')
    await daofanginfo[0].click()
    #输入案场名称

    #截图保存



#识别结果(时间段识别结果)
async def shibiejieguo(page):
    #进入识别结果
    shibieinfo = await page.xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[5]/li/span')
    await shibieinfo[0].click()
    #输入案场名称


    #输入识别结果开始时间

    #输入识别结果结束时间

    #截图保存


#主函数
async def main():
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://icloud.sensetime.com/senserealty/login')
    width, height = screen_size()
    print("获取屏幕长的值和类型",width,type(width))
    # 最大化窗口
    #await page.setViewport({width:width,height:height})
    await page.setViewport(viewport={'width': width, 'height':height})
    # 设置浏览器
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                ' Chrome/74.0.3729.169 Safari/537.36')
    # 防止被识别，将webdriver设置为false
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    #登录的用户名和密码
    await page.type('#BX_Layer2 > div > form > div > div > div > input', 'SKtest', {'delay': input_time_random() - 50})
    await page.type('.BX_Sprite2 .el-form .el-form-item:nth-child(2) .el-form-item__content .el-input__inner', 'SKtest123', {'delay': input_time_random()})
    # 登录时的验证
    normal_login = await page.xpath('//*[@id="BX_Layer2"]/div/form/div[4]/button')
    await normal_login[0].click()
    time.sleep(1)
    # 滑动验证
    await page.waitFor(1000)
    await try_validation(page)
    await page.waitFor(1000)
    await shibieguanli(page)
    await page.waitFor(1000)
    await qudaofengkong(page)
    await page.waitFor(2000)
    #图片保存
    await page.screenshot({'path': 'shibieguanli.png'})
    await page.close()


    

asyncio.get_event_loop().run_until_complete(main())