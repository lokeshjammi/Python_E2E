import time

from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Myntra")
        time.sleep(5)