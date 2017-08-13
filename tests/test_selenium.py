import unittest
from selenium import webdriver

browsers = []
browsers.append({'browser': 'Chrome'})
browsers.append({'browser': 'Firefox'})

for browser in browsers:
	if browser['browser'] == 'Chrome':
		driver = webdriver.Chrome()
	elif browser['browser'] == 'Firefox':
		driver = webdriver.Firefox()
	
	driver.implicitly_wait(30)
	 
	driver.get("http://www.google.com")
	 
	search_field = driver.find_element_by_id("lst-ib")
	search_field.clear()
	 
	search_field.send_keys("Selenium WebDriver Interview questions")
	search_field.submit()
	 
	lists= driver.find_elements_by_class_name("_Rm")
	 
	print ("Found " + str(len(lists)) + "searches:")
	 
	i=0
	for listitem in lists:
	   print (listitem)
	   i=i+1
	   if(i>10):
	      break
	 
	driver.quit()