from selenium import webdriver
from selenium.webdriver.common.by import By

def iniciarSesion(driver):
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com")
        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        btn_login = driver.find_element(By.ID,"login-button")
        
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        
        btn_login.click()

            
