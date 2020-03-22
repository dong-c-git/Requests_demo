import random

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


track_list=get_track(loc+3)
time.sleep(2)
ActionChains(driver).click_and_hold(slideblock).perform()
time.sleep(0.2)
# 根据轨迹拖拽圆球
for track in track_list:
    ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
# 模拟人工滑动超过缺口位置返回至缺口的情况，数据来源于人工滑动轨迹，同时还加入了随机数，都是为了更贴近人工滑动轨迹
imitate=ActionChains(driver).move_by_offset(xoffset=-1, yoffset=0)
time.sleep(0.015)
imitate.perform()
time.sleep(random.randint(6,10)/10)
imitate.perform()
time.sleep(0.04)
imitate.perform()
time.sleep(0.012)
imitate.perform()
time.sleep(0.019)
imitate.perform()
time.sleep(0.033)
ActionChains(driver).move_by_offset(xoffset=1, yoffset=0).perform()
# 放开圆球
ActionChains(driver).pause(random.randint(6,14)/10).release(slideblock).perform()
time.sleep(2)
#务必记得加入quit()或close()结束进程，不断测试电脑只会卡卡西
driver.close()


if __name__ == "__main__":
    get_track(305)