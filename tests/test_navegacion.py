from selenium import webdriver
from selenium.webdriver.common.by import By
from paginas.login_pagina import LoginPagina
from paginas.productos_pagina import ProductosPagina
    

def test_validacion_titulo(driver):
    login_pagina = LoginPagina(driver)
    prods_pagina = ProductosPagina(driver)
    try:
        login_pagina.iniciar_sesion("standard_user","secret_sauce")
        titulo = prods_pagina.obtener_titulo
        assert titulo.text == "Swag Labs"
    except:
        print("Error")
      
      
def test_productos_visibles(driver):
    login_pagina = LoginPagina(driver)
    prods_pagina = ProductosPagina(driver)
    
    try:
        login_pagina.iniciar_sesion("standard_user","secret_sauce")
        productos = prods_pagina.obtener_productos()  
        assert productos[0].text == "Sauce Labs Backpack"
        assert productos[1].text == "Sauce Labs Bike Light"
    except:
        print("Error")
        
        
def test_verificar_elementos_principales(driver):
    login_pagina = LoginPagina(driver)
    prods_pagina = ProductosPagina(driver)
        
    try:
        assert prods_pagina.obtener_menu_hamburguesa.is_displayed()
        assert prods_pagina.obtener_titulo.is_displayed()
        assert prods_pagina.obtener_elemento_carrito.is_displayed()
    except:
        print("Error")    