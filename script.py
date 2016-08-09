from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ff = webdriver.Remote(command_executor='http://172.17.0.5:4444/wd/hub', desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)

ff.get("https://www.hdi.global/de/en")
print(repr(ff.title))
assert "HDI Global" in ff.title

WebDriverWait(ff, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body .main input[name='q']")))

search_box = ff.find_element_by_css_selector("body .main input[name='q']")
search_box.send_keys("test")
search_box.send_keys("\n")

WebDriverWait(ff, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-filter-result a")))
assert ff.title == "Search results"
ff.find_element_by_css_selector(".search-filter-result a").click()


ff.close()
exit()
