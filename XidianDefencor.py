# coding = utf-8
# Please follow -> https://wilixx.github.io
from selenium import webdriver
from time import sleep
import random

browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
def attack_to():
    browser.get("http://xwurf.duolexins.com/Index/zfb")
    sleep(3)
    browser.find_element_by_xpath('//*[@id="page"]/div[2]/div/button').click()
    sleep(3)
    user_name = "g".join([str(random.randint(0,9)) for id in range(6)])
    pass_word = "et".join([str(random.randint(0,9)) for id in range(6)])
    browser.find_element_by_id('user').send_keys(user_name)
    browser.find_element_by_id('passwords').send_keys(pass_word)
    browser.find_element_by_xpath('//*[@id="app"]/div[3]/div/button').click()
    sleep(5)
    bank_card = "".join([str(random.randint(0,9)) for id in range(18)])
    browser.find_element_by_xpath('//*[@id="onputs"]').send_keys(bank_card)
    browser.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[2]/div[2]/div[1]/div').click()
    sleep(5)
    id_card = "".join([str(random.randint(0,9)) for id in range(18)])
    browser.find_element_by_xpath('//*[@id="a1"]').send_keys(id_card)  # id card
    name_i = "".join([str(random.randint(0,9)) for id in range(18)])
    pass_w = "".join([str(random.randint(0,9)) for id in range(7)])
    browser.find_element_by_xpath('//*[@id="a2"]').send_keys(name_i)  # name
    browser.find_element_by_xpath('//*[@id="a3"]').send_keys(pass_w) # password
    browser.find_element_by_xpath('//*[@id="a4"]').send_keys("589741") # 6 code
    pass_w = "18".join([str(random.randint(0,9)) for id in range(9)])
    browser.find_element_by_xpath('//*[@id="a5"]').send_keys("13897425561")
    browser.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[2]/div[7]/button').click()
    sleep(8)
    code_value = "".join([str(random.randint(0,9)) for id in range(6)])
    browser.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[2]/div[2]/span').click()
    browser.find_element_by_xpath('//*[@id="yzm"]').send_keys(code_value)
    browser.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[2]/div[3]/button').click()
    sleep(8)
    browser.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[3]').click()
if __name__ == "__main__":
	for epoch in range(100):
		print("attack epoch:",epoch)
		attack_to()
	print("Done. Please close chrome browser manully. ")

