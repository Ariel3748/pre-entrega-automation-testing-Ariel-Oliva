from selenium import webdriver
from selenium.webdriver.common.by import By

    
WEB = "https://www.saucedemo.com"


def test_login_exitoso():
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:
        driver.get(WEB)
        
        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        btn_login = driver.find_element(By.ID,"login-button")
        
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        
        btn_login.click()
        
        title = driver.find_element(By.CSS_SELECTOR,"[data-test='primary-header'] .app_logo")
        
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert title.text == "Swag Labs"
    finally:
        driver.quit()