from src.facturacion import calcular_factura

def test_descuento_antes_de_iva():
    productos = [
        {"nombre": "A", "precio": 100, "cantidad": 1},
        {"nombre": "B", "precio": 100, "cantidad": 1},
    ]
    # Subtotal = 200, descuento 10% => 180, IVA 19% => 214.2
    subtotal, iva, total = calcular_factura(productos, tasa_iva=0.19, descuento=0.10)
    assert subtotal == 200
    assert round(iva, 2) == 38.00  # IVA sobre 200 (como lo hace el modulo actual)
    # Pero el total correcto seria 214.2; este assert fallara por el bug intencional
    assert round(total, 1) == 214.2
