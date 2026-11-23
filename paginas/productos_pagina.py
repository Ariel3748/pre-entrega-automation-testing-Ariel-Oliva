from selenium.webdriver.common.by import By
from selenium import webdriver


class ProductosPagina:
    def __init__(self, driver):
        self.driver = driver
        
    def obtener_productos(self):
        ##Se tiene que haber iniciado sesion
        self.driver.implicitly_wait(10)
        productos = self.driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item-name']")
        return(productos)
    
    def obtener_titulo(self):
        ##Se tiene que haber iniciado sesion
        self.driver.implicity_wait(5)
        
        titulo = self.driver.find_element(By.CSS_SELECTOR,"[data-test='primary-header'] .app_logo")
        
        return(titulo)
    
    def obtener_menu_hamburguesa(self):
        ##Se tiene que haber iniciado sesion
        return self.driver.find_element(By.CSS_SELECTOR,"[data-test='open-menu']")
    
    def obtener_elemento_carrito(self):
        return(self.driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']"))