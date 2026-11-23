from selenium.webdriver.common.by import By
from selenium import webdriver




class CarritoPagina:
    def __init__(self,driver):
        self.driver = driver
        
    def agregar_primer_prod_al_carrito(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
    def obtener_carrito(self):
          self.driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']").click()
          
          return(self.driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item']"))
      
    def obtener_contador_carrito(self):
        return(self.driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))