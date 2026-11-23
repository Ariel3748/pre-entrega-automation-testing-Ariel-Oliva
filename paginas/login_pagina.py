from selenium.webdriver.common.by import By



class LoginPagina:
    def __init__(self, driver):
        self.driver = driver
    
    def iniciar_sesion(self, usuario, contrasena):
        self.driver.get("https://www.saucedemo.com")
        user = self.driver.find_element(By.ID,"user-name")
        password = self.driver.find_element(By.ID,"password")
        btn_login = self.driver.find_element(By.ID,"login-button")
        
        user.send_keys(usuario)
        password.send_keys(contrasena)
        
        btn_login.click()