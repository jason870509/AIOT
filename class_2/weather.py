from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import shutil
import os


def getLastestFileName():
    path = '/Users/wuyubin/Downloads'
    #
    try:
        fileName = max([f for f in os.listdir(path)],
                       key=lambda x: os.path.getmtime(os.path.join(path, x)))
        # f for f in os.listdir(path) 等於下面3行
        # fileList = []
        # for f in os.listdir(path):
        #     fileList.append(f)
    except:
        fileName = max([f for f in os.listdir(path)],
                       key=lambda x: os.path.getmtime(os.path.join(path, x)))
    return fileName


def changeName(finalName):
    # 偵測檔案是否下載完成，完成下載的檔名最後會是.csv
    while True:
        fileName = getLastestFileName()
        if fileName.endswith('.csv'):
            break
    path = '/Users/wuyubin/Downloads'
    # 更改檔名
    shutil.move(f'{path}\\{fileName}', f'{path}\\{finalName}')


browser = webdriver.Chrome('class_2/chromedriver')
browser.get('https://e-service.cwb.gov.tw/HistoryDataQuery/')

# 非同步式載入的網頁才要用while loop
while True:
    try:
        # 點選北部地區 id = Button_North
        browser.find_element_by_id('Button_North').click()
        break
    except:
        pass

time.sleep(2)

for item in Select(browser.find_element_by_id('stationCounty')).options:
    # Print(item.text)
    if item.text.find('新北市') != -1:
        # 選擇測站所在城市 id = stationCounty
        Select(browser.find_element_by_id('stationCounty'))\
            .select_by_visible_text(item.text)

for item in Select(browser.find_element_by_id('station')).options:
    # 選擇測站 id = station
    Select(browser.find_element_by_id('station'))\
        .select_by_visible_text(item.text)

    # 時間欄中輸入值 id = datepicker
    browser.find_element_by_id('datepicker').send_keys('2021-03-22')
    # 按下查詢按鈕 id = doquery
    browser.find_element_by_id('doquery').click()

    # 切換視窗到最後一個
    windows = browser.window_handles
    browser.switch_to_window(windows[-1])
    # 點選路徑為 xpath 的圖片
    browser.find_element_by_xpath(
        "//input[@src='images/downloadCSV_2.png']").click()

    # 關閉視窗
    browser.close()
    # 切換為原視窗
    browser.switch_to_window(windows[0])

    time.sleep(1)
    changeName(f"{item.text}.csv")
    break
