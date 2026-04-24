import random

# ══════════════════════════════════════════════════════════════════════════════
#  SOLUCIÓN — Ejercicio 12 — Sistema Bancario Completo
# ══════════════════════════════════════════════════════════════════════════════


# ── Excepciones personalizadas ────────────────────────────────────────────────

class BancoError(Exception):
    """Excepción base del sistema bancario."""
    pass

class SaldoInsuficienteError(BancoError):
    pass

class LimiteSuperadoError(BancoError):
    pass

class TarjetaBloqueadaError(BancoError):
    pass

class PrestamoError(BancoError):
    pass

class InversionError(BancoError):
    pass


# ── Transaccion ───────────────────────────────────────────────────────────────

class Transaccion:
    def __init__(self, tipo, monto, descripcion):
        self.tipo = tipo
        self.monto = monto
        self.descripcion = descripcion

    def __str__(self):
        signo = "+" if self.tipo in ("deposito", "transferencia_entrada") else "-"
        return f"[{self.tipo.upper()}] {signo}${self.monto:.2f} — {self.descripcion}"


# ── Cuenta (base) ─────────────────────────────────────────────────────────────

class Cuenta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0.0
        self.__historial = []

    def get_saldo(self):
        return self.__saldo

    def get_historial(self):
        return list(self.__historial)

    def depositar(self, monto, descripcion="Depósito"):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        self.__saldo += monto
        self.__historial.append(Transaccion("deposito", monto, descripcion))

    def _registrar_extraccion(self, monto, descripcion):
        self.__saldo -= monto
        self.__historial.append(Transaccion("extraccion", monto, descripcion))

    def extraer(self, monto, descripcion="Extracción"):
        raise NotImplementedError("Las subclases deben implementar extraer().")

    def _registrar_transferencia(self, monto, es_entrada, descripcion):
        if es_entrada:
            self.__saldo += monto
            self.__historial.append(Transaccion("transferencia_entrada", monto, descripcion))
        else:
            self.__saldo -= monto
            self.__historial.append(Transaccion("transferencia_salida", monto, descripcion))

    def __str__(self):
        return f"Cuenta #{self.numero} | Titular: {self.titular.nombre} | Saldo: ${self.__saldo:.2f}"


class CajaDeAhorro(Cuenta):
    def __init__(self, numero, titular):
        super().__init__(numero, titular)

    def extraer(self, monto, descripcion="Extracción"):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        if monto > self.get_saldo():
            raise SaldoInsuficienteError(
                f"Saldo insuficiente. Saldo actual: ${self.get_saldo():.2f}"
            )
        self._registrar_extraccion(monto, descripcion)


class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, limite_descubierto):
        super().__init__(numero, titular)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto, descripcion="Extracción"):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        if monto > self.get_disponible():
            raise LimiteSuperadoError(
                f"Límite de descubierto alcanzado. Disponible: ${self.get_disponible():.2f}"
            )
        self._registrar_extraccion(monto, descripcion)

    def get_disponible(self):
        return self.get_saldo() + self.limite_descubierto


# ── Tarjeta (base) ────────────────────────────────────────────────────────────

class Tarjeta:
    def __init__(self, numero, titular):
        self.__numero = numero
        self.titular = titular
        self.activa = True

    def get_numero_enmascarado(self):
        return f"****-****-****-{self.__numero[-4:]}"

    def bloquear(self):
        self.activa = False

    def desbloquear(self):
        self.activa = True

    def _validar_activa(self):
        if not self.activa:
            raise TarjetaBloqueadaError("Tarjeta bloqueada. No se puede operar.")

    def __str__(self):
        estado = "ACTIVA" if self.activa else "BLOQUEADA"
        return (
            f"Tarjeta [{self.get_numero_enmascarado()}] "
            f"| Titular: {self.titular.nombre} | Estado: {estado}"
        )


class TarjetaDebito(Tarjeta):
    def __init__(self, numero, cuenta):
        super().__init__(numero, cuenta.titular)
        self.cuenta = cuenta

    def pagar(self, monto, descripcion="Pago con débito"):
        self._validar_activa()
        self.cuenta.extraer(monto, descripcion)


class TarjetaCredito(Tarjeta):
    def __init__(self, numero, titular, limite):
        super().__init__(numero, titular)
        self.__limite = limite
        self.__deuda = 0.0
        self.seguros = []

    def get_deuda(self):
        return self.__deuda

    def get_limite_disponible(self):
        return self.__limite - self.__deuda

    def contratar_seguro(self, seguro):
        self.seguros.append(seguro)

    def cobrar_seguros(self, cuenta):
        for seguro in self.seguros:
            seguro.cobrar(cuenta)

    def pagar_con_tarjeta(self, monto, descripcion="Pago con crédito"):
        self._validar_activa()
        if monto > self.get_limite_disponible():
            raise LimiteSuperadoError(
                f"Límite de crédito insuficiente. Disponible: ${self.get_limite_disponible():.2f}"
            )
        self.__deuda += monto

    def pagar_deuda(self, monto, cuenta):
        if monto > self.__deuda:
            monto = self.__deuda
        cuenta.extraer(monto, "Pago de deuda de tarjeta de crédito")
        self.__deuda -= monto

    def __str__(self):
        return (
            f"TarjetaCredito [{self.get_numero_enmascarado()}] "
            f"| Deuda: ${self.__deuda:.2f} | Disponible: ${self.get_limite_disponible():.2f} "
            f"| Seguros activos: {sum(1 for s in self.seguros if s.activo)}"
        )


# ── Seguro ────────────────────────────────────────────────────────────────────

class Seguro:
    TIPOS_VALIDOS = ("robo", "fraude", "viaje")

    def __init__(self, tipo, costo_mensual):
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo de seguro inválido. Opciones: {self.TIPOS_VALIDOS}")
        self.tipo = tipo
        self.costo_mensual = costo_mensual
        self.activo = True

    def cancelar(self):
        if not self.activo:
            raise BancoError("El seguro ya está cancelado.")
        self.activo = False

    def cobrar(self, cuenta):
        if not self.activo:
            return
        try:
            cuenta.extraer(self.costo_mensual, f"Cobro mensual seguro de {self.tipo}")
            print(f"    Seguro '{self.tipo}' cobrado: ${self.costo_mensual:.2f}")
        except (SaldoInsuficienteError, LimiteSuperadoError) as e:
            print(f"    [Seguro] No se pudo cobrar el seguro de {self.tipo}: {e}")

    def __str__(self):
        estado = "ACTIVO" if self.activo else "CANCELADO"
        return f"Seguro de {self.tipo.upper()} | ${self.costo_mensual:.2f}/mes | {estado}"


# ── CuotaPrestamo ─────────────────────────────────────────────────────────────

class CuotaPrestamo:
    def __init__(self, numero, monto):
        self.numero = numero
        self.monto = monto
        self.pagada = False

    def pagar(self):
        if self.pagada:
            raise PrestamoError(f"La cuota #{self.numero:02d} ya fue pagada.")
        self.pagada = True

    def __str__(self):
        estado = "PAGADA" if self.pagada else "PENDIENTE"
        return f"Cuota #{self.numero:02d} | ${self.monto:.2f} | {estado}"


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
        monto_total = self.monto * (1 + self.tasa_mensual * self.cantidad_cuotas)
        monto_cuota = round(monto_total / self.cantidad_cuotas, 2)
        return [CuotaPrestamo(i + 1, monto_cuota) for i in range(self.cantidad_cuotas)]

    def acreditar(self):
        if not self.aprobado:
            raise PrestamoError("El préstamo no está aprobado.")
        self.cuenta_debito.depositar(self.monto, "Acreditación de préstamo aprobado")

    def pagar_cuota(self):
        if not self.aprobado:
            raise PrestamoError("El préstamo no está aprobado. No se pueden pagar cuotas.")
        for cuota in self.cuotas:
            if not cuota.pagada:
                self.cuenta_debito.extraer(cuota.monto, f"Cuota #{cuota.numero:02d} del préstamo")
                cuota.pagar()
                return cuota
        raise PrestamoError("Todas las cuotas ya fueron pagadas. El préstamo está saldado.")

    def cuotas_pendientes(self):
        return [c for c in self.cuotas if not c.pagada]

    def esta_saldado(self):
        return all(c.pagada for c in self.cuotas)

    def __str__(self):
        pendientes = len(self.cuotas_pendientes())
        estado = "APROBADO" if self.aprobado else "PENDIENTE APROBACIÓN"
        return (
            f"Préstamo ${self.monto:.2f} | Tasa: {self.tasa_mensual * 100:.1f}%/mes | "
            f"{pendientes}/{self.cantidad_cuotas} cuotas pendientes | {estado}"
        )


# ── Inversion ─────────────────────────────────────────────────────────────────

class Inversion:
    def __init__(self, monto, tasa_anual, meses, cuenta_origen):
        if monto <= 0:
            raise ValueError("El monto de inversión debe ser positivo.")
        if monto > cuenta_origen.get_saldo():
            raise SaldoInsuficienteError(
                f"Saldo insuficiente para invertir. Disponible: ${cuenta_origen.get_saldo():.2f}"
            )
        self.monto = monto
        self.tasa_anual = tasa_anual
        self.meses = meses
        self.cuenta_origen = cuenta_origen
        self.rescatada = False
        cuenta_origen.extraer(monto, f"Constitución de inversión a plazo fijo ({meses} meses)")

    def calcular_ganancia(self):
        return round(self.monto * (self.tasa_anual / 12) * self.meses, 2)

    def calcular_total(self):
        return round(self.monto + self.calcular_ganancia(), 2)

    def rescatar(self, cuenta_destino):
        if self.rescatada:
            raise InversionError("Esta inversión ya fue rescatada.")
        total = self.calcular_total()
        cuenta_destino.depositar(total, f"Rescate de inversión a plazo fijo ({self.meses} meses)")
        self.rescatada = True
        return total

    def __str__(self):
        estado = "RESCATADA" if self.rescatada else "ACTIVA"
        return (
            f"Inversión ${self.monto:.2f} | Tasa: {self.tasa_anual * 100:.0f}% anual | "
            f"{self.meses} meses | Ganancia estimada: ${self.calcular_ganancia():.2f} | {estado}"
        )


# ── Persona (base) ────────────────────────────────────────────────────────────

class Persona:
    def __init__(self, nombre, dni, email):
        self.nombre = nombre
        self.__dni = dni
        self.email = email

    def get_dni(self):
        return self.__dni

    def __str__(self):
        return f"{self.nombre} (DNI: {self.__dni})"


# ── Cliente (hereda de Persona) ───────────────────────────────────────────────

class Cliente(Persona):
    def __init__(self, nombre, dni, email):
        super().__init__(nombre, dni, email)
        self.cuentas = []
        self.tarjetas = []
        self.prestamos = []
        self.inversiones = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def agregar_tarjeta(self, tarjeta):
        self.tarjetas.append(tarjeta)

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def agregar_inversion(self, inversion):
        self.inversiones.append(inversion)

    def mostrar_resumen(self):
        print("=" * 50)
        print(f"  Cliente : {self.nombre}  |  DNI: {self.get_dni()}")
        print(f"  Email   : {self.email}")
        print("  ── Cuentas ──────────────────────────────────")
        if self.cuentas:
            for i, c in enumerate(self.cuentas):
                print(f"    [{i}] {c}")
        else:
            print("    Sin cuentas.")
        print("  ── Tarjetas ─────────────────────────────────")
        if self.tarjetas:
            for i, t in enumerate(self.tarjetas):
                print(f"    [{i}] {t}")
        else:
            print("    Sin tarjetas.")
        print("  ── Préstamos ────────────────────────────────")
        if self.prestamos:
            for i, p in enumerate(self.prestamos):
                print(f"    [{i}] {p}")
        else:
            print("    Sin préstamos.")
        print("  ── Inversiones ──────────────────────────────")
        if self.inversiones:
            for i, inv in enumerate(self.inversiones):
                print(f"    [{i}] {inv}")
        else:
            print("    Sin inversiones.")
        print("=" * 50)


# ── Empleado (hereda de Persona) ──────────────────────────────────────────────

class Empleado(Persona):
    def __init__(self, nombre, dni, email, legajo, sueldo):
        super().__init__(nombre, dni, email)
        self.legajo = legajo
        self.sueldo = sueldo
        self.sucursal = None

    def mostrar_datos(self):
        sucursal_str = self.sucursal.nombre if self.sucursal else "Sin sucursal"
        print(
            f"  {self.__class__.__name__} | {self.nombre} | Legajo: {self.legajo} | "
            f"Sueldo: ${self.sueldo:.2f} | Sucursal: {sucursal_str}"
        )

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} (Legajo: {self.legajo})"


# ── Cajero (hereda de Empleado) ───────────────────────────────────────────────

class Cajero(Empleado):
    def realizar_deposito(self, cuenta, monto, descripcion="Depósito en caja"):
        try:
            cuenta.depositar(monto, descripcion)
            print(f"  [Cajero {self.nombre}] Depósito de ${monto:.2f} OK → {cuenta}")
        except ValueError as e:
            print(f"  [Cajero {self.nombre}] Error en depósito: {e}")

    def realizar_extraccion(self, cuenta, monto, descripcion="Extracción en caja"):
        try:
            cuenta.extraer(monto, descripcion)
            print(f"  [Cajero {self.nombre}] Extracción de ${monto:.2f} OK → {cuenta}")
        except (SaldoInsuficienteError, LimiteSuperadoError) as e:
            print(f"  [Cajero {self.nombre}] Error en extracción: {e}")
        except ValueError as e:
            print(f"  [Cajero {self.nombre}] Monto inválido: {e}")


# ── Asesor (hereda de Empleado) ───────────────────────────────────────────────

class Asesor(Empleado):
    def abrir_caja_ahorro(self, banco, cliente):
        cuenta = banco.abrir_caja_ahorro(cliente)
        if self.sucursal:
            self.sucursal.registrar_cliente(cliente)
        print(f"  [Asesor {self.nombre}] CajaDeAhorro abierta para {cliente.nombre}: {cuenta}")
        return cuenta

    def abrir_cuenta_corriente(self, banco, cliente, limite_descubierto):
        cuenta = banco.abrir_cuenta_corriente(cliente, limite_descubierto)
        if self.sucursal:
            self.sucursal.registrar_cliente(cliente)
        print(f"  [Asesor {self.nombre}] CuentaCorriente abierta para {cliente.nombre}: {cuenta}")
        return cuenta

    def tramitar_prestamo(self, cliente, monto, tasa_mensual, cantidad_cuotas, cuenta):
        prestamo = Prestamo(monto, tasa_mensual, cantidad_cuotas, cuenta)
        cliente.agregar_prestamo(prestamo)
        print(
            f"  [Asesor {self.nombre}] Préstamo tramitado para {cliente.nombre}. "
            f"Pendiente de aprobación del gerente."
        )
        return prestamo

    def crear_inversion(self, cliente, monto, tasa_anual, meses, cuenta):
        try:
            inversion = Inversion(monto, tasa_anual, meses, cuenta)
            cliente.agregar_inversion(inversion)
            print(f"  [Asesor {self.nombre}] Inversión creada para {cliente.nombre}: {inversion}")
            return inversion
        except SaldoInsuficienteError as e:
            print(f"  [Asesor {self.nombre}] No se pudo crear la inversión: {e}")
            return None


# ── Gerente (hereda de Empleado) ──────────────────────────────────────────────

class Gerente(Empleado):
    def __init__(self, nombre, dni, email, legajo, sueldo):
        super().__init__(nombre, dni, email, legajo, sueldo)
        self.sucursal_a_cargo = None

    def asignar_sucursal(self, sucursal):
        self.sucursal_a_cargo = sucursal
        self.sucursal = sucursal
        sucursal.gerente = self

    def aprobar_prestamo(self, prestamo):
        try:
            if prestamo.aprobado:
                raise PrestamoError("El préstamo ya estaba aprobado.")
            prestamo.aprobado = True
            prestamo.acreditar()
            print(f"  [Gerente {self.nombre}] Préstamo aprobado y acreditado.")
        except PrestamoError as e:
            print(f"  [Gerente {self.nombre}] Error al aprobar: {e}")

    def informe_sucursal(self):
        if not self.sucursal_a_cargo:
            print(f"  [Gerente {self.nombre}] Sin sucursal asignada.")
            return
        self.sucursal_a_cargo.imprimir_informe()


# ── Sucursal ──────────────────────────────────────────────────────────────────

class Sucursal:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.empleados = []
        self.clientes_atendidos = []
        self.gerente = None

    def contratar_empleado(self, empleado):
        empleado.sucursal = self
        if isinstance(empleado, Gerente):
            self.gerente = empleado
        self.empleados.append(empleado)

    def registrar_cliente(self, cliente):
        if cliente not in self.clientes_atendidos:
            self.clientes_atendidos.append(cliente)

    def imprimir_informe(self):
        gerente_str = self.gerente.nombre if self.gerente else "Sin gerente"
        cajeros  = sum(1 for e in self.empleados if isinstance(e, Cajero))
        asesores = sum(1 for e in self.empleados if isinstance(e, Asesor))
        print(f"  ══ Informe Sucursal: {self.nombre} ══════════════════")
        print(f"  Dirección  : {self.direccion}")
        print(f"  Gerente    : {gerente_str}")
        print(f"  Empleados  : {len(self.empleados)}  (Cajeros: {cajeros} | Asesores: {asesores})")
        print(f"  Clientes   : {len(self.clientes_atendidos)}")
        for c in self.clientes_atendidos:
            print(f"    · {c}")

    def __str__(self):
        return f"Sucursal {self.nombre} | {self.direccion}"


# ── Banco ─────────────────────────────────────────────────────────────────────

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__clientes = []
        self.__cuentas = []
        self.__sucursales = []
        self.__contador_cuentas = 1

    def crear_sucursal(self, nombre, direccion):
        sucursal = Sucursal(nombre, direccion)
        self.__sucursales.append(sucursal)
        return sucursal

    def registrar_cliente(self, nombre, dni, email, sucursal=None):
        cliente = Cliente(nombre, dni, email)
        self.__clientes.append(cliente)
        if sucursal:
            sucursal.registrar_cliente(cliente)
        return cliente

    def abrir_caja_ahorro(self, cliente):
        numero = self._generar_numero_cuenta()
        cuenta = CajaDeAhorro(numero, cliente)
        self.__cuentas.append(cuenta)
        cliente.agregar_cuenta(cuenta)
        return cuenta

    def abrir_cuenta_corriente(self, cliente, limite_descubierto):
        numero = self._generar_numero_cuenta()
        cuenta = CuentaCorriente(numero, cliente, limite_descubierto)
        self.__cuentas.append(cuenta)
        cliente.agregar_cuenta(cuenta)
        return cuenta

    def emitir_tarjeta_debito(self, cuenta):
        if not isinstance(cuenta, CajaDeAhorro):
            raise TypeError("La tarjeta débito solo se puede emitir para una CajaDeAhorro.")
        tarjeta = TarjetaDebito(self._generar_numero_tarjeta(), cuenta)
        cuenta.titular.agregar_tarjeta(tarjeta)
        return tarjeta

    def emitir_tarjeta_credito(self, cliente, limite):
        tarjeta = TarjetaCredito(self._generar_numero_tarjeta(), cliente, limite)
        cliente.agregar_tarjeta(tarjeta)
        return tarjeta

    def transferir(self, cuenta_origen, cuenta_destino, monto):
        if cuenta_origen is cuenta_destino:
            raise ValueError("No se puede transferir a la misma cuenta.")
        if isinstance(cuenta_origen, CajaDeAhorro) and monto > cuenta_origen.get_saldo():
            raise SaldoInsuficienteError(
                f"Saldo insuficiente para transferir. Disponible: ${cuenta_origen.get_saldo():.2f}"
            )
        if isinstance(cuenta_origen, CuentaCorriente) and monto > cuenta_origen.get_disponible():
            raise LimiteSuperadoError(
                f"Límite superado en cuenta origen. Disponible: ${cuenta_origen.get_disponible():.2f}"
            )
        cuenta_origen._registrar_transferencia(monto, False, f"Transferencia a #{cuenta_destino.numero}")
        cuenta_destino._registrar_transferencia(monto, True, f"Transferencia desde #{cuenta_origen.numero}")

    def buscar_cliente_por_dni(self, dni):
        for cliente in self.__clientes:
            if cliente.get_dni() == dni:
                return cliente
        return None

    def listar_clientes(self):
        for c in self.__clientes:
            print(f"  {c}")

    def listar_sucursales(self):
        for s in self.__sucursales:
            print(f"  {s}")

    def _generar_numero_cuenta(self):
        numero = str(self.__contador_cuentas).zfill(4)
        self.__contador_cuentas += 1
        return numero

    def _generar_numero_tarjeta(self):
        return "".join([str(random.randint(0, 9)) for _ in range(16)])
