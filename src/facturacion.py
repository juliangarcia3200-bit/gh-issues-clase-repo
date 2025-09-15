"""
Modulo de facturacion.
- Aplica IVA y descuentos.
- BUG intencional: el descuento se aplica despues del IVA.
"""
from typing import List, Dict, Tuple

def calcular_factura(productos: List[Dict], tasa_iva: float = 0.19, descuento: float = 0.0) -> Tuple[float, float, float]:
    """
    Calcula subtotal, iva y total con descuento.
    :param productos: lista de dicts con keys: nombre, precio, cantidad
    :param tasa_iva: 0.19 para 19%
    :param descuento: 0.10 para 10%
    :return: (subtotal, iva, total_final)
    """
    if not 0 <= descuento < 1:
        raise ValueError("El descuento debe estar entre 0 y 1 (ej. 0.10 para 10%).")
    if tasa_iva < 0:
        raise ValueError("La tasa de IVA debe ser >= 0.")

    subtotal = 0.0
    for p in productos:
        precio = float(p.get("precio", 0))
        cantidad = int(p.get("cantidad", 0))
        if precio < 0 or cantidad < 0:
            raise ValueError("Precio y cantidad deben ser >= 0.")
        subtotal += precio * cantidad

    iva = round(subtotal * tasa_iva, 2)

    # BUG: descuento despues del IVA (deberia ser antes)
    total = subtotal + iva
    total_final = round(total * (1 - descuento), 2)

    return round(subtotal, 2), iva, total_final
