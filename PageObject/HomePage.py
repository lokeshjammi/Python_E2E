from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        return self.driver.findelement(*HomePage.shop) #When * is used, shop tuple is converted to driver.findelement(By.CSS_SELECTOR, "a[href*='shop']"
