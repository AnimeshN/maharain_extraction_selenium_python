import bs4 as bs
# # import urlib.request
from urllib.request import urlopen

# sauce = urlopen('http://maharain.gov.in').read()

# soup = bs.BeautifulSoup(sauce,'lxml')

# print(soup)

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
# binary = FirefoxBinary('/usr/bin/firefox')

driver = webdriver.Firefox(executable_path='./geckodriver')

driver.get('http://maharain.gov.in')
# driver.maximize_window()


# driver.find_element_by_css_selector(".mmenu[value='PastQueriesCirclewise6']").click()
# driver.find_element_by_xpath("//input[@type='submit' and @value='PastQueriesCirclewise6']").click()
driver.switch_to.frame("MenuFrame")
driver.find_element_by_name("PastQueriesCirclewise6").click()
driver.find_element_by_xpath("//input[@type='button' and @value='Daily Rain']").click()
#selecting  dropdown 

driver.switch_to.default_content()

driver.switch_to.frame("ContentFrame")

Select(driver.find_element_by_name("selyear")).select_by_index(1)
Select(driver.find_element_by_name("selstate")).select_by_index(1)
Select(driver.find_element_by_name("seldist")).select_by_index(1)
Select(driver.find_element_by_name("selmonth")).select_by_index(1)

driver.find_element_by_name("btnshow").click()

driver.get('view-source:http://maharain.gov.in/RainPastDailyMonth.php')

# table_id = inputElement = driver.find_element_by_id("tableID")
# driver.find_element_by_tag_name("table")




# select_element = Select(driver.find_element_by_id("selyear"))
# print ([option.text for option in select_element.options])

# driver.switchTo().frame(framename);
# driver.switchTo.frame(int index);
# soup = bs(html)
# soup = bs.BeautifulSoup(html,'lxml')
# driver.switch_to.frame(1)
# table  = driver.find_element_by_id("tableID")
# print(table.text)

# driver.switch_to.default_content()
# from selenium.webdriver.common.keys import Keys
# driver.find_element_by_tag_name('frame').send_keys(Keys.CONTROL + Keys.SHIFT + 'E')
# from selenium.webdriver import ActionChains

# actionChain = ActionChains(driver)
# element = driver.find_element_by_tag_name("table")
# actionChain.context_click().perform()
# actionChain.move_by_offset(element, 150, 1000) #move 150 pixels to the right to access Help link
# import pyautogui
# x, y = pyautogui.position()
# print('X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4))
# pyautogui.rightClick(406, 856)
# pyautogui.moveTo(501, 762, duration=0.01)
# pyautogui.rightClick(10, 5)
html = driver.page_source

from selenium.webdriver.common.keys import Keys

elem = driver.find_element_by_tag_name("body")
elem.send_keys("bar")
elem.send_keys(Keys.CONTROL, 'a') #highlight all in box
elem.send_keys(Keys.CONTROL, 'c') #copy

from tkinter import Tk
from time import sleep
r = Tk()
r.withdraw()

while not r.selection_get(selection="CLIPBOARD"):
    sleep(0.1)

result = r.selection_get(selection = "CLIPBOARD")
r.clipboard_clear()
r.destroy
print(result)
file1 = open("MyFile.txt","w")
file1.write(result) 
file1.close()
