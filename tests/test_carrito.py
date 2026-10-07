from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.iniciarSesion import iniciarSesion


def test_agregar_producto_al_carrito():
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    try:
        iniciarSesion(driver)
        
        botonAddToCart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        
        botonAddToCart.click()
        
        carrito = driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']")
        
        carrito.click()
        
        pirmerElementoCarrito = driver.find_element(By.CSS_SELECTOR,"[data-test='inventory-item-name']")
        
        assert pirmerElementoCarrito.text == "Sauce Labs Backpack"
    finally:
        driver.close()
        
        
def test_contador_de_carrito():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    try:
        iniciarSesion(driver)
        
        botonAddToCart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        
        botonAddToCart.click()
        
        cantCarrito = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
        
        assert cantCarrito.text == '1'
        
    finally:
        driver.quit()