from src.amortizacion import cuota_fija

def test_cuota_fija_porcentaje():
    # Para 1'000.000 a 20% anual a 12 meses, la cuota con tasa mensual 0.20/12 aprox. 92,235.29
    cuota = cuota_fija(1_000_000, 20, 12)  # tasa_anual en porcentaje
    assert round(cuota, 2) == 92235.29  # Este assert fallara por el bug intencional
