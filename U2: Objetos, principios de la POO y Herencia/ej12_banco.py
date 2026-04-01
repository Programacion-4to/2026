import random

# ══════════════════════════════════════════════════════════════════════════════
#  Ejercicio 12 — Sistema Bancario Completo
#  Completá cada clase. Cuando termines ejecutá ej12_banco_runner.py
# ══════════════════════════════════════════════════════════════════════════════


# ── Excepciones personalizadas ────────────────────────────────────────────────

class BancoError(Exception):
    """Excepción base del sistema bancario."""
    pass

class SaldoInsuficienteError(BancoError):
    # Se lanza cuando no hay fondos suficientes para una operación
    pass

class LimiteSuperadoError(BancoError):
    # Se lanza cuando se supera el límite de descubierto o de crédito
    pass

class TarjetaBloqueadaError(BancoError):
    # Se lanza cuando se intenta operar con una tarjeta bloqueada
    pass

class PrestamoError(BancoError):
    # Se lanza cuando hay un error en operaciones de préstamo
    pass

class InversionError(BancoError):
    # Se lanza cuando hay un error en operaciones de inversión
    pass


# ── Transaccion ───────────────────────────────────────────────────────────────

class Transaccion:
    def __init__(self, tipo, monto, descripcion):
        self.tipo = tipo
        self.monto = monto
        self.descripcion = descripcion

    def __str__(self):
        pass


# ── Cuenta (base) ─────────────────────────────────────────────────────────────

class Cuenta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0.0
        self.__historial = []

    def get_saldo(self):
        pass

    def get_historial(self):
        pass

    def depositar(self, monto, descripcion="Depósito"):
        pass

    def _registrar_extraccion(self, monto, descripcion):
        pass

    def extraer(self, monto, descripcion="Extracción"):
        raise NotImplementedError("Las subclases deben implementar extraer().")

    def _registrar_transferencia(self, monto, es_entrada, descripcion):
        pass

    def __str__(self):
        pass


class CajaDeAhorro(Cuenta):
    def __init__(self, numero, titular):
        pass

    def extraer(self, monto, descripcion="Extracción"):
        pass


class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, limite_descubierto):
        pass

    def extraer(self, monto, descripcion="Extracción"):
        pass

    def get_disponible(self):
        pass


# ── Tarjeta (base) ────────────────────────────────────────────────────────────

class Tarjeta:
    def __init__(self, numero, titular):
        self.__numero = numero
        self.titular = titular
        self.activa = True

    def get_numero_enmascarado(self):
        pass

    def bloquear(self):
        pass

    def desbloquear(self):
        pass

    def _validar_activa(self):
        pass

    def __str__(self):
        pass


class TarjetaDebito(Tarjeta):
    def __init__(self, numero, cuenta):
        pass

    def pagar(self, monto, descripcion="Pago con débito"):
        pass


class TarjetaCredito(Tarjeta):
    def __init__(self, numero, titular, limite):
        pass

    def get_deuda(self):
        pass

    def get_limite_disponible(self):
        pass

    def contratar_seguro(self, seguro):
        pass

    def cobrar_seguros(self, cuenta):
        pass

    def pagar_con_tarjeta(self, monto, descripcion="Pago con crédito"):
        pass

    def pagar_deuda(self, monto, cuenta):
        pass

    def __str__(self):
        pass


# ── Seguro ────────────────────────────────────────────────────────────────────

class Seguro:
    TIPOS_VALIDOS = ("robo", "fraude", "viaje")

    def __init__(self, tipo, costo_mensual):
        pass

    def cancelar(self):
        pass

    def cobrar(self, cuenta):
        pass

    def __str__(self):
        pass


# ── CuotaPrestamo ─────────────────────────────────────────────────────────────

class CuotaPrestamo:
    def __init__(self, numero, monto):
        self.numero = numero
        self.monto = monto
        self.pagada = False

    def pagar(self):
        pass

    def __str__(self):
        pass


# ── Prestamo ──────────────────────────────────────────────────────────────────

class Prestamo:
    def __init__(self, monto, tasa_mensual, cantidad_cuotas, cuenta_debito):
        self.monto = monto
        self.tasa_mensual = tasa_mensual
        self.cantidad_cuotas = cantidad_cuotas
        self.cuenta_debito = cuenta_debito
        self.aprobado = False
        self.cuotas = self._generar_cuotas()

    def _generar_cuotas(self):
        pass

    def acreditar(self):
        pass

    def pagar_cuota(self):
        pass

    def cuotas_pendientes(self):
        pass

    def esta_saldado(self):
        pass

    def __str__(self):
        pass


# ── Inversion ─────────────────────────────────────────────────────────────────

class Inversion:
    def __init__(self, monto, tasa_anual, meses, cuenta_origen):
        pass

    def calcular_ganancia(self):
        pass

    def calcular_total(self):
        pass

    def rescatar(self, cuenta_destino):
        pass

    def __str__(self):
        pass


# ── Persona (base) ────────────────────────────────────────────────────────────

class Persona:
    def __init__(self, nombre, dni, email):
        self.nombre = nombre
        self.__dni = dni
        self.email = email

    def get_dni(self):
        pass

    def __str__(self):
        pass


# ── Cliente (hereda de Persona) ───────────────────────────────────────────────

class Cliente(Persona):
    def __init__(self, nombre, dni, email):
        pass

    def agregar_cuenta(self, cuenta):
        pass

    def agregar_tarjeta(self, tarjeta):
        pass

    def agregar_prestamo(self, prestamo):
        pass

    def agregar_inversion(self, inversion):
        pass

    def mostrar_resumen(self):
        pass


# ── Empleado (hereda de Persona) ──────────────────────────────────────────────

class Empleado(Persona):
    def __init__(self, nombre, dni, email, legajo, sueldo):
        pass

    def mostrar_datos(self):
        pass

    def __str__(self):
        pass


# ── Cajero (hereda de Empleado) ───────────────────────────────────────────────

class Cajero(Empleado):
    def realizar_deposito(self, cuenta, monto, descripcion="Depósito en caja"):
        pass

    def realizar_extraccion(self, cuenta, monto, descripcion="Extracción en caja"):
        pass


# ── Asesor (hereda de Empleado) ───────────────────────────────────────────────

class Asesor(Empleado):
    def abrir_caja_ahorro(self, banco, cliente):
        pass

    def abrir_cuenta_corriente(self, banco, cliente, limite_descubierto):
        pass

    def tramitar_prestamo(self, cliente, monto, tasa_mensual, cantidad_cuotas, cuenta):
        pass

    def crear_inversion(self, cliente, monto, tasa_anual, meses, cuenta):
        pass


# ── Gerente (hereda de Empleado) ──────────────────────────────────────────────

class Gerente(Empleado):
    def __init__(self, nombre, dni, email, legajo, sueldo):
        pass

    def asignar_sucursal(self, sucursal):
        pass

    def aprobar_prestamo(self, prestamo):
        pass

    def informe_sucursal(self):
        pass


# ── Sucursal ──────────────────────────────────────────────────────────────────

class Sucursal:
    def __init__(self, nombre, direccion):
        pass

    def contratar_empleado(self, empleado):
        pass

    def registrar_cliente(self, cliente):
        pass

    def imprimir_informe(self):
        pass

    def __str__(self):
        pass


# ── Banco ─────────────────────────────────────────────────────────────────────

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__clientes = []
        self.__cuentas = []
        self.__sucursales = []
        self.__contador_cuentas = 1

    def crear_sucursal(self, nombre, direccion):
        pass

    def registrar_cliente(self, nombre, dni, email, sucursal=None):
        pass

    def abrir_caja_ahorro(self, cliente):
        pass

    def abrir_cuenta_corriente(self, cliente, limite_descubierto):
        pass

    def emitir_tarjeta_debito(self, cuenta):
        pass

    def emitir_tarjeta_credito(self, cliente, limite):
        pass

    def transferir(self, cuenta_origen, cuenta_destino, monto):
        pass

    def buscar_cliente_por_dni(self, dni):
        pass

    def listar_clientes(self):
        pass

    def listar_sucursales(self):
        pass

    def _generar_numero_cuenta(self):
        pass

    def _generar_numero_tarjeta(self):
        pass
