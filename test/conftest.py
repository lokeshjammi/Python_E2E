import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service = Service("D:\Python_Workspace\Python_Automation\Drivers\Edge\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://www.google.com")
    request.cls.driver = driver
    yield
    driver.quit()