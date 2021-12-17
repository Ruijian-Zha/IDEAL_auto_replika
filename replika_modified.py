#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"

path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

browser = webdriver.Chrome(path) #谷歌

#browser = webdriver.Firefox()
browser.get("https://my.replika.ai/login")
browser.find_element_by_id("emailOrPhone").send_keys("xxxxxx@163.com")
#通过id = kw定位百度输入框，通过键盘方法send_keys()向输入框中输入selenium。
browser.find_element_by_id("emailOrPhone").send_keys(Keys.ENTER)
#browser.find_element_by_id("root").click()
#通过id=su定位搜索按钮，并向按钮发送单击事件click()
import time
time.sleep(1)
browser.find_element_by_id("login-password").send_keys('xxxx_password_xxxx')
browser.find_element_by_id("login-password").send_keys(Keys.ENTER)

while(True):
    # ask for an input string form user
    string = input("User: ")

    browser.find_element_by_id("send-message-textarea").send_keys(string)
    browser.find_element_by_id("send-message-textarea").send_keys(Keys.ENTER)
    #browser.quit()

    # a=browser.find_element_by_id("message-61b05194c8c5bc00072eed64-text").text
    
    fiveth_item = browser.find_elements_by_xpath("//*[contains(@id, '-text')]")
    len(fiveth_item)
    last=fiveth_item[-1].text
    if last=='':
        last=fiveth_item[-2].text

    sixth_item = browser.find_elements_by_xpath("//*[contains(@id, '-text')]")
    the_len = len(sixth_item)
    answer_len = 0
    while(True):
        time.sleep(1)
        if(len(browser.find_elements_by_xpath("//*[contains(@id, '-text')]")) > the_len+1):
            answer_len = len(browser.find_elements_by_xpath("//*[contains(@id, '-text')]")) - the_len
            break
        
    ## unlock 2 possible answers but uncomment it
    # time.sleep(3)

    sixth_item = browser.find_elements_by_xpath("//*[contains(@id, '-text')]")
    len(sixth_item)
    str=sixth_item[-1].text
    if str=='':
        str=sixth_item[-2].text
        if last == sixth_item[-4].text:
            print("Replika: " + str)
        else:
            print("Replika: " + sixth_item[-3].text)
            print("Replika: " + str)
    else:
        if last == sixth_item[-3].text:
            print("Replika: " + str)
        else:
            print("Replika: " + sixth_item[-2].text)
            print("Replika: " + str)

    # str=sixth_item[-2].text
    # if str=='':
    #     str=sixth_item[-3].text
    #     if last == sixth_item[-4].text:
    #         print("Replika: " + str)
    #     else:
    #         print("Replika: " + sixth_item[-4].text)
    #         print("Replika: " + str)
    # else:
    #     if last == sixth_item[-3].text:
    #         print("Replika: " + str)
    #     else:
    #         print("Replika: " + sixth_item[-3].text)
    #         print("Replika: " + str)