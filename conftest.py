import pytest   
from selenium import webdriver
##Para correr el programa usar python -m pytest
WEB = "https://www.saucedemo.com"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(WEB)
    yield driver
    
    driver.quit()
    
    
