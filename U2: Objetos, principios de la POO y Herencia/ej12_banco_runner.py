# ── Runner — Sistema Bancario Completo ────────────────────────────────────────
# Ejecutá este archivo para probar tu implementación de ej12_banco.py.
# ─────────────────────────────────────────────────────────────────────────────

from ej12_banco import (
    Banco, Sucursal,
    CajaDeAhorro, CuentaCorriente,
    TarjetaDebito, TarjetaCredito,
    Seguro, CuotaPrestamo, Prestamo, Inversion,
    Cajero, Asesor, Gerente, Cliente,
    BancoError, SaldoInsuficienteError, LimiteSuperadoError,
    TarjetaBloqueadaError, PrestamoError, InversionError,
)


def titulo(texto):
    print(f"\n{'─' * 3} {texto} {'─' * max(0, 52 - len(texto))}")


# ════════════════════════════════════════════════════════
# 1. Crear banco y sucursales
# ════════════════════════════════════════════════════════
titulo("1. Banco y sucursales")

banco = Banco("Banco Pythón")
sucursal_centro = banco.crear_sucursal("Centro", "Av. Corrientes 1234")
sucursal_norte  = banco.crear_sucursal("Norte",  "Av. Libertador 5678")

banco.listar_sucursales()
# Esperado:
#   Sucursal Centro | Av. Corrientes 1234
#   Sucursal Norte  | Av. Libertador 5678


# ════════════════════════════════════════════════════════
# 2. Contratar empleados
# ════════════════════════════════════════════════════════
titulo("2. Contratar empleados")

gerente = Gerente("María Gómez",  "30111222", "maria@banco.com", "G001", 200000)
asesor  = Asesor ("Juan López",   "31222333", "juan@banco.com",  "A001", 120000)
cajera  = Cajero ("Ana Pérez",    "32333444", "ana@banco.com",   "C001",  90000)

sucursal_centro.contratar_empleado(gerente)
sucursal_centro.contratar_empleado(asesor)
sucursal_centro.contratar_empleado(cajera)

gerente.asignar_sucursal(sucursal_centro)

gerente.mostrar_datos()
asesor.mostrar_datos()
cajera.mostrar_datos()
# Esperado: cada empleado muestra nombre, legajo, sueldo y sucursal Centro


# ════════════════════════════════════════════════════════
# 3. Registrar clientes
# ════════════════════════════════════════════════════════
titulo("3. Registrar clientes")

pedro = banco.registrar_cliente("Pedro Sánchez",  "40123456", "pedro@mail.com", sucursal_centro)
lucia = banco.registrar_cliente("Lucía Martínez", "41234567", "lucia@mail.com", sucursal_centro)

banco.listar_clientes()
# Esperado:
#   Pedro Sánchez (DNI: 40123456)
#   Lucía Martínez (DNI: 41234567)


# ════════════════════════════════════════════════════════
# 4. Asesor abre cuentas
# ════════════════════════════════════════════════════════
titulo("4. Abrir cuentas (vía asesor)")

ahorro_pedro    = asesor.abrir_caja_ahorro(banco, pedro)
corriente_pedro = asesor.abrir_cuenta_corriente(banco, pedro, 8000.0)
ahorro_lucia    = asesor.abrir_caja_ahorro(banco, lucia)

print(ahorro_pedro)     # Cuenta #0001 | Titular: Pedro Sánchez | Saldo: $0.00
print(corriente_pedro)  # Cuenta #0002 | Titular: Pedro Sánchez | Saldo: $0.00
print(ahorro_lucia)     # Cuenta #0003 | Titular: Lucía Martínez | Saldo: $0.00


# ════════════════════════════════════════════════════════
# 5. Cajera hace depósitos
# ════════════════════════════════════════════════════════
titulo("5. Depósitos (vía cajera)")

cajera.realizar_deposito(ahorro_pedro, 50000, "Acreditación sueldo")
cajera.realizar_deposito(ahorro_lucia, 20000, "Acreditación sueldo")
cajera.realizar_deposito(ahorro_pedro, -500, "Monto inválido")   # debe mostrar error, no explotar

print(ahorro_pedro)   # Saldo: $50000.00
print(ahorro_lucia)   # Saldo: $20000.00


# ════════════════════════════════════════════════════════
# 6. Cajera hace extracciones
# ════════════════════════════════════════════════════════
titulo("6. Extracciones (vía cajera)")

cajera.realizar_extraccion(ahorro_pedro, 5000, "Retiro en caja")
cajera.realizar_extraccion(ahorro_lucia, 99999, "Intento sin fondos")     # error esperado
cajera.realizar_extraccion(ahorro_pedro, -200, "Monto negativo inválido") # error esperado

print(ahorro_pedro)   # Saldo: $45000.00


# ════════════════════════════════════════════════════════
# 7. Tarjetas
# ════════════════════════════════════════════════════════
titulo("7. Emitir tarjetas")

# Débito solo para CajaDeAhorro
try:
    banco.emitir_tarjeta_debito(corriente_pedro)
except TypeError as e:
    print(f"[ERROR esperado] {e}")

debito_pedro  = banco.emitir_tarjeta_debito(ahorro_pedro)
credito_pedro = banco.emitir_tarjeta_credito(pedro, 30000.0)

print(debito_pedro)
print(credito_pedro)

# Pago con débito
debito_pedro.pagar(3000, "Supermercado")
print(ahorro_pedro)   # Saldo bajó $3000

# Bloquear y reintentar
debito_pedro.bloquear()
try:
    debito_pedro.pagar(100, "Intento con tarjeta bloqueada")
except TarjetaBloqueadaError as e:
    print(f"[ERROR esperado] {e}")
debito_pedro.desbloquear()


# ════════════════════════════════════════════════════════
# 8. Seguros en tarjeta de crédito
# ════════════════════════════════════════════════════════
titulo("8. Seguros")

# Tipo inválido
try:
    seguro_malo = Seguro("hipoteca", 300.0)
except ValueError as e:
    print(f"[ERROR esperado] {e}")

seguro_fraude = Seguro("fraude", 500.0)
seguro_robo   = Seguro("robo",   300.0)
credito_pedro.contratar_seguro(seguro_fraude)
credito_pedro.contratar_seguro(seguro_robo)

print(credito_pedro)  # Seguros activos: 2

# Cobrar seguros desde la cuenta de ahorro
credito_pedro.cobrar_seguros(ahorro_pedro)
print(ahorro_pedro)   # Saldo bajó $800

# Cancelar uno y cobrar de nuevo
seguro_fraude.cancelar()
try:
    seguro_fraude.cancelar()   # ya cancelado
except BancoError as e:
    print(f"[ERROR esperado] {e}")

credito_pedro.cobrar_seguros(ahorro_pedro)  # solo cobra el de robo ($300)
print(ahorro_pedro)


# ════════════════════════════════════════════════════════
# 9. Pagos con tarjeta de crédito
# ════════════════════════════════════════════════════════
titulo("9. Pagos con tarjeta de crédito")

credito_pedro.pagar_con_tarjeta(10000, "Electrónica")
credito_pedro.pagar_con_tarjeta(8000,  "Vacaciones")
print(credito_pedro)  # Deuda: $18000 | Disponible: $12000

# Superar límite
try:
    credito_pedro.pagar_con_tarjeta(15000, "Demasiado caro")
except LimiteSuperadoError as e:
    print(f"[ERROR esperado] {e}")

# Pagar deuda
credito_pedro.pagar_deuda(18000, ahorro_pedro)
print(credito_pedro)   # Deuda: $0.00 | Disponible: $30000.00


# ════════════════════════════════════════════════════════
# 10. Préstamo
# ════════════════════════════════════════════════════════
titulo("10. Préstamo")

prestamo = asesor.tramitar_prestamo(pedro, 100000, 0.03, 12, ahorro_pedro)
print(prestamo)  # PENDIENTE APROBACIÓN

# Intentar pagar sin aprobar
try:
    prestamo.pagar_cuota()
except PrestamoError as e:
    print(f"[ERROR esperado] {e}")

# El gerente aprueba y acredita el monto en la cuenta
gerente.aprobar_prestamo(prestamo)
print(ahorro_pedro)   # Saldo aumentó $100000

# Intentar aprobar de nuevo (el gerente captura el error internamente)
gerente.aprobar_prestamo(prestamo)

# Pagar 3 cuotas
for _ in range(3):
    cuota = prestamo.pagar_cuota()
    print(cuota)

print(prestamo)   # 9/12 cuotas pendientes
print(f"¿Saldado? {prestamo.esta_saldado()}")   # False


# ════════════════════════════════════════════════════════
# 11. Inversión a plazo fijo
# ════════════════════════════════════════════════════════
titulo("11. Inversión a plazo fijo")

# Intentar invertir más de lo disponible (el asesor captura el error internamente)
inv_fallida = asesor.crear_inversion(pedro, 9999999, 0.60, 12, ahorro_pedro)
print(inv_fallida)   # None

inversion = asesor.crear_inversion(pedro, 20000, 0.60, 6, ahorro_pedro)
print(inversion)     # ACTIVA | Ganancia estimada: $6000.00

total = inversion.rescatar(ahorro_pedro)
print(f"Rescate total: ${total:.2f}")   # $26000.00
print(ahorro_pedro)

# Intentar rescatar de nuevo
try:
    inversion.rescatar(ahorro_pedro)
except InversionError as e:
    print(f"[ERROR esperado] {e}")

print(inversion)   # RESCATADA


# ════════════════════════════════════════════════════════
# 12. Transferencia entre cuentas
# ════════════════════════════════════════════════════════
titulo("12. Transferencia")

banco.transferir(ahorro_pedro, ahorro_lucia, 5000)
print(ahorro_pedro)   # bajó $5000
print(ahorro_lucia)   # subió $5000

# Misma cuenta
try:
    banco.transferir(ahorro_pedro, ahorro_pedro, 100)
except ValueError as e:
    print(f"[ERROR esperado] {e}")

# Sin fondos suficientes
try:
    banco.transferir(ahorro_lucia, ahorro_pedro, 999999)
except SaldoInsuficienteError as e:
    print(f"[ERROR esperado] {e}")


# ════════════════════════════════════════════════════════
# 13. Historial de transacciones
# ════════════════════════════════════════════════════════
titulo("13. Historial de Pedro (caja de ahorro)")

for t in ahorro_pedro.get_historial():
    print(f"  {t}")


# ════════════════════════════════════════════════════════
# 14. Informe de sucursal
# ════════════════════════════════════════════════════════
titulo("14. Informe de sucursal (vía gerente)")

gerente.informe_sucursal()
# Esperado: 3 empleados (1 cajero, 1 asesor, 1 gerente), 2 clientes


# ════════════════════════════════════════════════════════
# 15. Resúmenes de clientes
# ════════════════════════════════════════════════════════
titulo("15. Resumen de Pedro")
pedro.mostrar_resumen()

titulo("15. Resumen de Lucía")
lucia.mostrar_resumen()


# ════════════════════════════════════════════════════════
# 16. Búsqueda por DNI
# ════════════════════════════════════════════════════════
titulo("16. Búsqueda por DNI")

encontrado = banco.buscar_cliente_por_dni("41234567")
print(encontrado)   # Lucía Martínez (DNI: 41234567)

no_existe = banco.buscar_cliente_por_dni("00000000")
print(no_existe)   # None

print("\n¡Todos los casos funcionaron correctamente!")
