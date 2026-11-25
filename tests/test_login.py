from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.reader import reader_users_csv

from paginas.login_pagina import LoginPagina
    
WEB = "https://www.saucedemo.com"

        
@pytest.mark.parametrize("data",reader_users_csv())
def test_login(driver, data):
    login_pagina = LoginPagina(driver) 
    login_pagina.iniciar_sesion(data["user"],data["password"])
    
    es_valido = data["isValid"].strip().lower() == "true"
    if es_valido:
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert login_pagina.obtener_titulo().text == "Swag Labs"
    else:
        assert login_pagina.obtener_cartel_error().is_displayed()
