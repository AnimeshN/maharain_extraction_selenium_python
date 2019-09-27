import bs4 as bs
# # import urlib.request
from urllib.request import urlopen

# sauce = urlopen('http://maharain.gov.in').read()

# soup = bs.BeautifulSoup(sauce,'lxml')

# print(soup)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
# binary = FirefoxBinary('/usr/bin/firefox')

from tkinter import Tk
from time import sleep
import csv


# driver.maximize_window()


# driver.find_element_by_css_selector(".mmenu[value='PastQueriesCirclewise6']").click()
# driver.find_element_by_xpath("//input[@type='submit' and @value='PastQueriesCirclewise6']").click()

#selecting  dropdown 


# selyear = [1998]
# selstate = "Maharashtra"
# seldist = "Nasik"
# selmonth = "June"


# selyears = ["1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]
selyears = ["2012","2013","2014","2015","2016","2017","2018"]
selstates = "Maharashtra"
seldists = "Nasik"
selmonths = ["January","February","March","April","May","June","July","August","September","October","November","December"]
# selmonths = ["October","November","December"]
# selyears = ["2018"]

driver = webdriver.Firefox(executable_path='./geckodriver')


for year in selyears:
    for month in selmonths:

        driver.get('http://maharain.gov.in')
        sleep(2) 

        driver.switch_to.frame("MenuFrame")
        driver.find_element_by_name("PastQueriesTehsilwise6").click()
        driver.find_element_by_xpath("//input[@type='button' and @value='Daily Rain']").click()

        driver.switch_to.default_content()

        driver.switch_to.frame("ContentFrame")
        sleep(2) 

        Select(driver.find_element_by_name("selyear")).select_by_visible_text(year)
        # Select(driver.find_element_by_name("selstate")).select_by_visible_text(selstates)
        # Select(driver.find_element_by_name("seldist")).select_by_visible_text(seldists)
        Select(driver.find_element_by_name("selmonth")).select_by_visible_text(month)
        
        driver.find_element_by_name("btnshow").click()
        driver.get('view-source:http://maharain.gov.in/RainPastDailyTehsilMonth.php')
        elem = driver.find_element_by_tag_name("body")
        elem.send_keys("bar")
        elem.send_keys(Keys.CONTROL, 'a') #highlight all in box
        elem.send_keys(Keys.CONTROL, 'c') #copy

        # html = driver.page_source
        # print(html)
        r = Tk()

        r.withdraw()

        while not r.selection_get(selection="CLIPBOARD"):
            sleep(0.1)

        result = r.selection_get(selection = "CLIPBOARD")
        print(result)
        # r.clipboard_clear()
        soup = bs.BeautifulSoup(result,'lxml')

        table = soup.find("table")
        if(table):
            output_rows = []
            for table_row in table.findAll('tr'):
                columns = table_row.findAll('td')
                output_row = []
                for column in columns:
                    output_row.append(column.text)
                output_rows.append(output_row)
                
            with open(str(year) + "_"+ selstates + "_" + seldists + "_" + month + ".csv","w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(output_rows)


        # r.destroy
        # driver.close()

        # (str(year) + "_"+ selstate + "_" + seldist + "_" + month + ".html\n")



# Select(driver.find_element_by_name("selyear")).select_by_index(1)


# year = driver.find_element_by_name("selyear").get_attribute("attribute name")


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





# print(result)



# print(soup)





# driver.close()

# file1 = open(str(selyear) + "_"+ selstate + "_" + seldist + "_" + selmonth + ".html","w")
# file1.write(result) 
# file1.close()


