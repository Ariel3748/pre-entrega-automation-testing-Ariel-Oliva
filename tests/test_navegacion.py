from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.iniciarSesion import iniciarSesion
    
WEB = "https://www.saucedemo.com"

def test_validacion_titulo():
    
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

        assert title.text == "Swag Labs"
    finally:
      driver.quit()
      
      
def test_productos_visibles():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    try:
        iniciarSesion(driver)
        primerProducto = driver.find_element(By.CSS_SELECTOR,"[data-test='inventory-item-name']")
        segundoProducto = driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item-name']")[1]
        
        assert primerProducto.text == "Sauce Labs Backpack"
        assert segundoProducto.text == "Sauce Labs Bike Light"
    finally:
        driver.quit()
        
        
def test_verificar_elementos_principales():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
        
    try:
        iniciarSesion(driver)
        
        menuHamburguesa = driver.find_element(By.CSS_SELECTOR,"[data-test='open-menu']")
        title = driver.find_element(By.CSS_SELECTOR,"[data-test='primary-header'] .app_logo")
        carrito = driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']")
        
        assert menuHamburguesa.is_displayed()
        assert title.is_displayed()
        assert carrito.is_displayed()
    finally:
        driver.quit()    