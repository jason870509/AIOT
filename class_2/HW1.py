from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome('class_2/chromedriver')
browser.get('https://aiot.kaitechstudio.com')

username = 'ttu610906003'

browser.find_element_by_name('userID').send_keys(username)
browser.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(0.6)

T = 0
while(T < 200):
    T += 1
    answer = browser.find_element_by_id('Q1').get_attribute('value')
    answer = answer.replace(' ', '')
    answer = answer.replace('|', username)
    browser.find_element_by_id('Q1a').send_keys(answer)

    answer = browser.find_element_by_id('Q2').get_attribute('value')
    print(answer)
    answer = answer.split(' ')
    print(answer)

    if(answer[1] == '+'):
        answer2 = int(answer[0]) + int(answer[2])
    elif(answer[1] == '-'):
        answer2 = int(answer[0]) - int(answer[2])
    elif(answer[1] == '*'):
        answer2 = int(answer[0]) * int(answer[2])
    elif(answer[1] == '%'):
        answer2 = int(answer[0]) % int(answer[2])

    browser.find_element_by_id('Q2a').send_keys(answer2)

    browser.find_element_by_id('btnSubmit').click()

    time.sleep(0.6)

browser.refresh()
# for item in Select(browser.find_element_by_id('stationCounty')).options:
#     # Print(item.text)
#     if item.text.find('新北市') != -1:
#         # 選擇測站所在城市 id = stationCounty
#         Select(browser.find_element_by_id('stationCounty'))\
#             .select_by_visible_text(item.text)

# for item in Select(browser.find_element_by_id('station')).options:
#     # 選擇測站 id = station
#     Select(browser.find_element_by_id('station'))\
#         .select_by_visible_text(item.text)
