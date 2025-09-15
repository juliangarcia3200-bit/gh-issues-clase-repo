import pandas as pd
from pathlib import Path
from .facturacion import calcular_factura
from .amortizacion import cuota_fija

DATA = Path(__file__).resolve().parent.parent / "data" / "productos.csv"

def demo_facturacion():
    df = pd.read_csv(DATA)
    productos = df.to_dict(orient="records")
    subtotal, iva, total = calcular_factura(productos, tasa_iva=0.19, descuento=0.10)
    print("=== FACTURACION ===")
    print(f"Subtotal: {subtotal:,.2f}")
    print(f"IVA (19%): {iva:,.2f}")
    print(f"Total (con 10% de descuento): {total:,.2f}")
    print()

def demo_amortizacion():
    monto = 1_000_000
    tasa_anual = 20  # 20% anual (porcentaje)
    meses = 12
    cuota = cuota_fija(monto, tasa_anual, meses)
    print("=== AMORTIZACION ===")
    print(f"Monto: {monto:,.0f} | Tasa anual: {tasa_anual}% | Plazo: {meses} meses")
    print(f"Cuota fija mensual: {cuota:,.2f}")

if __name__ == "__main__":
    demo_facturacion()
    demo_amortizacion()
