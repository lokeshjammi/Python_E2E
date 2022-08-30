import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default = "chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getOption("--browser_name")
    if browser_name == "edge":
        service = Service("D:\Python_Workspace\Python_Automation\Drivers\Edge\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        driver.maximize_window()
        driver.get("https://www.google.com")
        request.cls.driver = driver
        yield
        driver.quit()
    elif browser_name == "chrome":
        service = Service("D:\Python_Workspace\Python_Automation\Drivers\chrome\chrome.exe")
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get("https://www.google.com")
        return driver