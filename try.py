from selenium import webdriver



driver = webdriver.PhantomJS()
driver.set_window_size(800, 600)
driver.get('https://www.google.fi')
data = driver.find_element_by_id("_eEe").text
print data

