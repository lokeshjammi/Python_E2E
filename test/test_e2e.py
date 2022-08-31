import time

from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self, cls=None):
        homepage = HomePage(self.driver)
        homepage.shop.click()
        time.sleep(5)