from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class wp:
    def __init__(self):
        #enter the driver path
        self.driver = webdriver.Chrome(executable_path='')
        self.driver.get("https://web.whatsapp.com")
        time.sleep(20)

    # def openn(self):
    # 	time.sleep(10)
    # 	self.driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]').click()
    # 	time.sleep(3)


    def msg(self):
    	while True:
    		# time.sleep(5)
	    	self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("BITCH")
	    	self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)

if __name__ == '__main__':
	w = wp()
	# w.openn()
	time.sleep(10)
	w.msg()
