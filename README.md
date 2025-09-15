# Sistema Contable (Repositorio de practica para Issues)

Este repositorio esta disenado para tu clase sobre GitHub Issues. Incluye errores intencionales y oportunidades de mejora
para que tus estudiantes creen Issues, los etiqueten y los conecten a Pull Requests.

## Contexto
Una pyme necesita:
1) Calcular facturas con IVA y descuentos.
2) Generar la cuota mensual de un credito (amortizacion francesa).

Hay bugs intencionales y detalles mejorables. El objetivo es detectarlos, reportarlos y proponer soluciones via Issues.

## Como ejecutar
```
pip install -r requirements.txt
python -m src.main
```

## Pruebas (opcionales)
```
python -m pytest -q
```
Incluye pruebas simples que fallaran por los errores intencionales.

## Archivos clave
- src/facturacion.py: calculo de subtotal, IVA y descuentos (bug de orden de operaciones).
- src/amortizacion.py: calculo de cuota fija (bug en la interpretacion de la tasa anual).
- data/productos.csv: datos de ejemplo para facturacion.
- tests/test_facturacion.py: valida el orden correcto de descuento e IVA.
- tests/test_amortizacion.py: valida la cuota con tasa anual dada en porcentaje.

## Actividad para crear Issues (sugerencias)
Crea al menos 6 Issues. Propuestas:
1. Bug: Descuento aplicado despues del IVA en facturacion.py. Esperado: aplicar descuento antes del IVA: total = (subtotal * (1 - d)) * (1 + iva)
2. Bug: Interpretacion de tasa_anual en amortizacion.py. El docstring dice porcentaje (ej. 20), pero el codigo lo trata como decimal (ej. 0.20).
3. Mejora: Redondeo y control de decimales coherente con contabilidad (usar Decimal).
4. Mejora: Validaciones de entrada (cantidades negativas, meses=0, etc.).
5. Docs: Aclarar con ejemplos el orden correcto de descuento/IVA y la unidad de la tasa.
6. Test: Casos limites (tasa 0, un solo producto, gran volumen, descuento 100%).

Conecta tu PR a cada Issue con "Closes #N" en el mensaje.

## Flujo sugerido
1. Cada estudiante crea 1 Issue y etiqueta (bug, enhancement, documentation, tests).
2. Asigna el Issue a un companero.
3. Abran un Project (Kanban) y muevan las tarjetas por columnas.
4. Implementen la solucion en una rama, abran un PR y cierren el Issue automaticamente con "Closes #N".
