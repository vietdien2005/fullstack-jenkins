# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import unittest, time, re

# desired_cap = []
# desired_cap.append({'browser': 'Chrome'})
# desired_cap.append({'browser': 'Firefox'})

# for driver_instance in desired_cap:
# 	driver_instance['browserstack.debug'] = True
# 	driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=driver_instance)
	
# 	driver.implicitly_wait(30)
	 
# 	driver.get("http://www.google.com")
	 
# 	search_field = driver.find_element_by_id("lst-ib")
# 	search_field.clear()
	 
# 	search_field.send_keys("Jenkins Selenium WebDriver")
# 	search_field.submit()
	 
# 	lists= driver.find_elements_by_class_name("_Rm")
	 
# 	print ("Found " + str(len(lists)) + "searches:")
	 
# 	i=0
# 	for listitem in lists:
# 	   print (listitem)
# 	   i=i+1
# 	   if(i>10):
# 	      break
	 
# 	driver.quit()



from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities.CHROME
capabilities.update({'logLevel' : 'ERROR'})

driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
driver.get('http://stackoverflow.com/')

# chrome = webdriver.Remote(
#           command_executor='http://localhost:4444/wd/hub',
#           desired_capabilities=DesiredCapabilities.CHROME)

# firefox = webdriver.Remote(
#           command_executor='http://localhost:4444/wd/hub',
#           desired_capabilities=DesiredCapabilities.FIREFOX) 

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    desired_capabilities=DesiredCapabilities.CHROME)

# driver.get('https://devvui.com')
# print(driver.title)
# driver.quit()

# chrome.get('https://www.google.com')
# print(chrome.title)

# firefox.get('https://www.google.com')
# print(firefox.title)

# chrome.quit()
# firefox.quit()

