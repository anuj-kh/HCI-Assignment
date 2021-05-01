# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestFlipkartUser2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_flipkartUser2(self):
    self.driver.get("https://www.flipkart.com/")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.CSS_SELECTOR, ".eFQ30H:nth-child(3) .xtXmba").click()
    self.driver.execute_script("window.scrollTo(0,3932)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_167Mu3:nth-child(5) .\\_4921Z:nth-child(2) .\\_24_Dny").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_167Mu3:nth-child(6) .\\_4921Z:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_167Mu3:nth-child(6) .\\_4921Z:nth-child(6) .\\_24_Dny").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) .\\_4rR01T").click()
    self.vars["win8443"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.switch_to.window(self.vars["win8443"])
    self.vars["win3633"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win3633"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["win8443"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(9) .\\_4rR01T").click()
    self.vars["win6357"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win6357"])
    self.driver.find_element(By.ID, "pincodeInputId").click()
    self.driver.find_element(By.ID, "pincodeInputId").send_keys("390011")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2P_LDn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_20cDxP").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1KAjNd").click()
    self.driver.execute_script("window.scrollTo(0,1200)")
    self.driver.find_element(By.CSS_SELECTOR, ".P9aMAP > .q6DClP").click()
    self.driver.find_element(By.CSS_SELECTOR, ".P9aMAP > .q6DClP").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,100)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3v1-ww").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3v1-ww")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1-GQyH").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3SkBxJ").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2zbf83").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2zbf83").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_2zbf83")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2zbf83").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2zbf83").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2zbf83").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_2zbf83")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li > span").click()
    self.driver.find_element(By.CSS_SELECTOR, "li > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li > span")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2zbf83").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_6t1WkM").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3X7Jj1 > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3X7Jj1 > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3X7Jj1 > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3X7Jj1 > span")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3X7Jj1 > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3X7Jj1 > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_I_XQO").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_I_XQO").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_I_XQO")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_I_XQO").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2zbf83").click()
  