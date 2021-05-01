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

class TestFlipkartUser1():
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
  
  def test_flipkartUser1(self):
    self.driver.get("https://www.flipkart.com/")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.CSS_SELECTOR, ".eFQ30H:nth-child(3) .\\_396cs4").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_167Mu3:nth-child(6) .\\_4921Z:nth-child(6) .\\_24_Dny").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2yz7eI").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_167Mu3:nth-child(5) .\\_4921Z:nth-child(2) .\\_24_Dny").click()
    self.driver.find_element(By.CSS_SELECTOR, ".QvtND5 > span").click()
    self.driver.execute_script("window.scrollTo(0,584)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_38vbm7:nth-child(29) .\\_24_Dny").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3BBnX4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3BBnX4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3BBnX4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_38vbm7:nth-child(42) .\\_24_Dny").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3BBnX4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3BBnX4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3BBnX4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2BRIel").click()
    self.driver.find_element(By.CSS_SELECTOR, ".QvtND5 > span").click()
    self.driver.execute_script("window.scrollTo(0,584)")
    self.driver.execute_script("window.scrollTo(0,684)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_38vbm7:nth-child(29) .\\_24_Dny").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_38vbm7:nth-child(42) .\\_24_Dny").click()
    self.driver.find_element(By.CSS_SELECTOR, ".THxusM").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1ftpgI:nth-child(1)").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2GoDe3 > .\\_1YokD2:nth-child(1)").click()
    self.vars["win9231"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win9231"])
    self.driver.switch_to.window(self.vars["root"])
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.switch_to.window(self.vars["win9231"])
    self.vars["win8203"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win8203"])
    self.driver.switch_to.window(self.vars["win9231"])
    self.driver.switch_to.window(self.vars["win8203"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["win9231"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(17) .\\_4rR01T").click()
    self.vars["win7695"] = self.wait_for_window(2000)
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(17) .\\_4rR01T")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.switch_to.window(self.vars["win7695"])
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1FH0tX").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_1FH0tX")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3k-BhJ:nth-child(3) .\\_1s_Smc:nth-child(1) .\\_21lJbe").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3k-BhJ:nth-child(3) .\\_1s_Smc:nth-child(1) .\\_21lJbe")
    actions = ActionChains(self.driver)
    actions.
    (element).perform()
    self.driver.execute_script("window.scrollTo(0,100)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3v1-ww").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3v1-ww > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3v1-ww > span")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.execute_script("window.scrollTo(0,0)")
    self.vars["win9080"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win9080"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["win7695"])
    element = self.driver.find_element(By.LINK_TEXT, "Explore Plus")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3SkBxJ > span").click()
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    element = self.driver.find_element(By.LINK_TEXT, "Login")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1Z69nn").send_keys("7265034642")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3mctLh").send_keys("preetthakkar482000")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2doB4z").click()
  
