"""
Calculo de cuota fija (amortizacion francesa).

Se espera que `tasa_anual` sea un porcentaje (ej. 20 para 20%).

BUG intencional: el calculo usa `tasa_anual/12` sin convertir a decimal (deberia ser `(tasa_anual/100)/12`).
"""
def cuota_fija(monto: float, tasa_anual: float, meses: int) -> float:
    if meses <= 0:
        raise ValueError("Los meses deben ser > 0.")
    if monto < 0:
        raise ValueError("El monto debe ser >= 0.")

    # Interpretacion incorrecta de tasa mensual
    i = (tasa_anual/100) / 12

    # Caso borde (tasa 0) — tambien esta mal si tasa_anual es 0
    if i == 0:
        return round(monto / meses, 2)

    cuota = monto * (i * (1 + i) ** meses) / ((1 + i) ** meses - 1)
    return round(cuota, 2)
