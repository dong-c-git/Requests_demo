#conding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,random


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

#options.add_argument('disable-infobars')   #新版本chrome已经废弃
#options.add_argument('User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')
options.add_argument('--user-data-dir=/Users/dongchao/Library/Application Support/Google/Chrome/Default')
driver = webdriver.Chrome(options=options)

#参考方案2
#option = webdriver.ChromeOptions()
#option.add_argument('--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data')
#browser = webdriver.Chrome(chrome_options=option)

# #去除控制提示：
# option = webdriver.ChromeOptions()
# option.add_argument('disable-infobars')
# #option.add_argument('disable-infobars')
# #驱动部分
# driver = webdriver.Chrome(chrome_options=option)
driver.get("https://icloud.sensetime.com/sensego/2.0/web/console/ui/#/store/operate")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="BX_Layer2"]/div/form/div[1]/div/div/input').send_keys("SKtest")
driver.find_element_by_xpath('//*[@id="BX_Layer2"]/div/form/div[2]/div/div/input').send_keys('SKtest123')
driver.find_element_by_xpath('//*[@id="BX_Layer2"]/div/form/div[4]/button').click()
time.sleep(2)
#定位滑块
slideblock = driver.find_element_by_id("nc_1__bg")
slideblock2 = driver.find_element_by_id("nc_1_n1z")

#方案一：直接滑动到终点：
# 鼠标点击圆球不松开
#ActionChains(driver).click_and_hold(slideblock2).perform()
# 将圆球滑至相对起点位置的最右边
# ActionChains(driver).move_by_offset(xoffset=305, yoffset=0).perform()
time.sleep(10)
#方案二：轨迹滑动
def get_track(distance):
    track=[]
    current=0
    mid=distance*3/4
    t=random.randint(2,3)/10
    v=0
    while current<distance:
          if current<mid:
             a=2
          else:
             a=-3
          v0=v
          v=v0+a*t
          move=v0*t+1/2*a*t*t
          current+=move
          track.append(round(move))
    print(track)
    return track
track_list=get_track(305+3)
time.sleep(2)
# #按住滑块：
# ActionChains(driver).click_and_hold(slideblock2).perform()
# time.sleep(0.2)
# # 根据轨迹拖拽圆球
# for track in track_list:
#     ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
# # 模拟人工滑动超过缺口位置返回至缺口的情况，数据来源于人工滑动轨迹，同时还加入了随机数，都是为了更贴近人工滑动轨迹
# imitate=ActionChains(driver).move_by_offset(xoffset=-1, yoffset=0)
# time.sleep(0.0015)
# imitate.perform()
# time.sleep(random.randint(6,10)/10)
# imitate.perform()
# time.sleep(0.004)
# imitate.perform()
# time.sleep(0.0012)
# imitate.perform()
# time.sleep(0.0019)
# imitate.perform()
# time.sleep(0.0033)
# ActionChains(driver).move_by_offset(xoffset=1, yoffset=0).perform()
# # 放开圆球
# ActionChains(driver).pause(random.randint(6,14)/10).release(slideblock).perform()
time.sleep(2)
#务必记得加入quit()或close()结束进程，不断测试电脑只会卡卡西
#driver.close()

