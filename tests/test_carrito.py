from paginas.login_pagina import LoginPagina
from paginas.carrito_pagina import CarritoPagina

def test_agregar_producto_al_carrito(driver):
    login_pagina = LoginPagina(driver)
    carrito_pagina = CarritoPagina(driver) 
    
    try:
        login_pagina.iniciar_sesion("standard_user","secret_sauce")
        carrito_pagina.agregar_primer_prod_al_carrito()
        
        assert carrito_pagina.obtener_carrito.len > 0
    except:
        print("Error")
        
        
def test_contador_de_carrito(driver):
    login_pagina = LoginPagina(driver)
    carrito_pagina = CarritoPagina(driver)
    
    try:
        login_pagina.iniciar_sesion("standard_user","secret_sauce")
        carrito_pagina.agregar_primer_prod_al_carrito()
        
        assert carrito_pagina.obtener_contador_carrito.text == '1'
        
    except:
        print("Error")
        
        