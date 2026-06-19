import tkinter as tk
from tkinter import messagebox, simpledialog

from ej12_banco_SOLUCION import (
    Banco,
    CajaDeAhorro,
    TarjetaDebito,
    TarjetaCredito,
    Gerente,
    Asesor,
    Cajero,
    BancoError,
)


ML_YELLOW = "#F58220"
ML_BLUE = "#0B2E6F"
ML_BG = "#F3F6FB"
ML_WHITE = "#FFFFFF"
ML_DARK = "#14213D"
ML_LIGHT = "#EAF0FA"
ML_RED = "#C62828"
ML_GREEN = "#1B8A5A"

FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_LABEL = ("Segoe UI", 11)
FONT_BOLD = ("Segoe UI", 11, "bold")
FONT_SMALL = ("Segoe UI", 9)
FONT_BUTTON = ("Segoe UI", 10, "bold")


def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()


class BancoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Banco Galicia - Home Banking")
        self.geometry("980x620")
        self.resizable(False, False)
        self.configure(bg=ML_BG)

        self.main_frame = tk.Frame(self, bg=ML_BG)
        self.main_frame.pack(fill="both", expand=True)

        self._bootstrap_data()
        self.usuario_actual = None
        self.show_login()

    def _bootstrap_data(self):
        self.banco = Banco("Banco Galicia")
        self.sucursal = self.banco.crear_sucursal("Centro", "Av. Corrientes 1234")

        self.gerente = Gerente("Maria Gomez", "30111222", "maria@banco.com", "G001", 200000)
        self.asesor = Asesor("Juan Lopez", "31222333", "juan@banco.com", "A001", 120000)
        self.cajera = Cajero("Ana Perez", "32333444", "ana@banco.com", "C001", 90000)

        self.sucursal.contratar_empleado(self.gerente)
        self.sucursal.contratar_empleado(self.asesor)
        self.sucursal.contratar_empleado(self.cajera)
        self.gerente.asignar_sucursal(self.sucursal)

        pedro = self.banco.registrar_cliente("Pedro Sanchez", "40123456", "pedro@mail.com", self.sucursal)
        lucia = self.banco.registrar_cliente("Lucia Martinez", "41234567", "lucia@mail.com", self.sucursal)
        self.clientes = [pedro, lucia]

        ahorro_pedro = self.asesor.abrir_caja_ahorro(self.banco, pedro)
        self.asesor.abrir_cuenta_corriente(self.banco, pedro, 8000)
        ahorro_lucia = self.asesor.abrir_caja_ahorro(self.banco, lucia)

        self.cajera.realizar_deposito(ahorro_pedro, 50000, "Acreditacion sueldo")
        self.cajera.realizar_deposito(ahorro_lucia, 20000, "Acreditacion sueldo")

        self.banco.emitir_tarjeta_debito(ahorro_pedro)
        self.banco.emitir_tarjeta_credito(pedro, 30000)

        self.usuarios_login = {
            "cliente1": {"password": "1234", "rol": "cliente", "obj": pedro},
            "cliente2": {"password": "lu1234", "rol": "cliente", "obj": lucia},
            "admin": {"password": "admin123", "rol": "admin", "obj": self.gerente},
        }

    def _make_header(self, subtitulo):
        accent = tk.Frame(self.main_frame, bg=ML_YELLOW, height=6)
        accent.pack(fill="x")

        header = tk.Frame(self.main_frame, bg=ML_BLUE, height=60)
        header.pack(fill="x")

        tk.Label(
            header,
            text="GALICIA",
            font=("Segoe UI", 16, "bold"),
            bg=ML_BLUE,
            fg=ML_YELLOW,
        ).pack(side="left", padx=16, pady=12)

        tk.Label(header, text=subtitulo, font=FONT_LABEL, bg=ML_BLUE, fg=ML_WHITE).pack(
            side="left"
        )

        tk.Button(
            header,
            text="Cerrar sesion",
            font=FONT_SMALL,
            bg=ML_YELLOW,
            fg=ML_DARK,
            relief="flat",
            cursor="hand2",
            command=self.show_login,
        ).pack(side="right", padx=16, pady=14)

    def _obtener_cuenta_por_numero(self, numero):
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.numero == numero:
                    return cuenta
        return None

    def _mostrar_error(self, exc):
        messagebox.showerror("Error", str(exc))

    def show_login(self):
        clear(self.main_frame)
        self.usuario_actual = None

        accent = tk.Frame(self.main_frame, bg=ML_YELLOW, height=6)
        accent.pack(fill="x")

        header = tk.Frame(self.main_frame, bg=ML_BLUE, height=90)
        header.pack(fill="x")
        tk.Label(
            header,
            text="GALICIA",
            font=("Segoe UI", 26, "bold"),
            bg=ML_BLUE,
            fg=ML_YELLOW,
        ).pack(pady=(14, 0))
        tk.Label(
            header,
            text="Home Banking",
            font=FONT_LABEL,
            bg=ML_BLUE,
            fg=ML_WHITE,
        ).pack(pady=(0, 10))

        card = tk.Frame(self.main_frame, bg=ML_WHITE, padx=44, pady=34, highlightthickness=1, highlightbackground="#D7E1F4")
        card.pack(pady=50, ipadx=20, ipady=10)

        tk.Label(card, text="Ingresar al portal", font=FONT_TITLE, bg=ML_WHITE, fg=ML_DARK).grid(
            row=0, column=0, pady=(0, 20)
        )

        tk.Label(card, text="Usuario", font=FONT_LABEL, bg=ML_WHITE, fg=ML_DARK).grid(
            row=1, column=0, sticky="w"
        )
        user_entry = tk.Entry(card, font=FONT_LABEL, width=28, relief="solid", bd=1)
        user_entry.grid(row=2, column=0, pady=(4, 14), ipady=6)

        tk.Label(card, text="Contrasena", font=FONT_LABEL, bg=ML_WHITE, fg=ML_DARK).grid(
            row=3, column=0, sticky="w"
        )
        pass_entry = tk.Entry(card, font=FONT_LABEL, width=28, show="*", relief="solid", bd=1)
        pass_entry.grid(row=4, column=0, pady=(4, 20), ipady=6)

        def do_login():
            usuario = user_entry.get().strip().lower()
            contrasena = pass_entry.get()
            data = self.usuarios_login.get(usuario)

            if not data or data["password"] != contrasena:
                messagebox.showerror("Error", "Usuario o contrasena incorrectos")
                return

            self.usuario_actual = data
            if data["rol"] == "admin":
                self.show_admin()
            else:
                self.show_cliente()

        tk.Button(
            card,
            text="Ingresar",
            font=FONT_BUTTON,
            bg=ML_YELLOW,
            fg=ML_DARK,
            activebackground="#E27A1F",
            activeforeground=ML_WHITE,
            relief="flat",
            cursor="hand2",
            width=24,
            pady=8,
            command=do_login,
        ).grid(row=5, column=0, pady=(0, 6))

        tk.Label(
            self.main_frame,
            text="Demo Cliente: cliente / 1234    |    Demo Admin: admin / admin123",
            font=FONT_SMALL,
            bg=ML_BG,
            fg="#56637D",
        ).pack()

    def show_cliente(self):
        clear(self.main_frame)
        cliente = self.usuario_actual["obj"]
        self._make_header(f"Hola, {cliente.nombre}")

        body = tk.Frame(self.main_frame, bg=ML_BG)
        body.pack(fill="both", expand=True, padx=20, pady=12)

        left = tk.Frame(body, bg=ML_WHITE)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=4)

        right = tk.Frame(body, bg=ML_WHITE, width=280)
        right.pack(side="right", fill="y", pady=4)
        right.pack_propagate(False)

        tk.Label(left, text="Mis cuentas", font=FONT_BOLD, bg=ML_WHITE, fg=ML_DARK).pack(
            pady=(12, 6)
        )

        cuentas_list = tk.Listbox(left, font=FONT_LABEL, relief="solid", bd=1, height=8)
        cuentas_list.pack(fill="x", padx=12)

        historial = tk.Text(left, font=FONT_SMALL, relief="solid", bd=1, height=14)
        historial.pack(fill="both", expand=True, padx=12, pady=(10, 12))

        botones = tk.Frame(left, bg=ML_WHITE)
        botones.pack(fill="x", padx=12, pady=(0, 12))

        resumen_lbl = tk.Label(right, text="", font=FONT_LABEL, bg=ML_WHITE, fg=ML_DARK, justify="left")
        resumen_lbl.pack(fill="x", padx=12, pady=(14, 10))

        def cuenta_seleccionada():
            if not cliente.cuentas:
                return None
            seleccion = cuentas_list.curselection()
            if not seleccion:
                cuentas_list.selection_set(0)
                return cliente.cuentas[0]
            return cliente.cuentas[seleccion[0]]

        def refresh_historial(*_):
            cuenta = cuenta_seleccionada()
            historial.config(state="normal")
            historial.delete("1.0", "end")
            if cuenta is None:
                historial.insert("end", "No tenes cuentas todavia.")
                historial.config(state="disabled")
                return

            movimientos = cuenta.get_historial()
            if not movimientos:
                historial.insert("end", "Sin movimientos aun.")
            else:
                for mov in movimientos[-14:]:
                    historial.insert("end", f"{mov}\n")
            historial.config(state="disabled")

        def refresh_resumen():
            total = sum(c.get_saldo() for c in cliente.cuentas)
            tarjetas = len(cliente.tarjetas)
            prestamos_pend = sum(1 for p in cliente.prestamos if not p.aprobado)
            inversiones_activas = sum(1 for i in cliente.inversiones if not i.rescatada)

            resumen_lbl.config(
                text=(
                    f"Saldo total: ${total:.2f}\n"
                    f"Tarjetas: {tarjetas}\n"
                    f"Prestamos pendientes: {prestamos_pend}\n"
                    f"Inversiones activas: {inversiones_activas}"
                )
            )

        def refresh_cuentas():
            cuentas_list.delete(0, "end")
            for cuenta in cliente.cuentas:
                cuentas_list.insert(
                    "end",
                    f"#{cuenta.numero} | {cuenta.__class__.__name__} | Saldo ${cuenta.get_saldo():.2f}",
                )
            if cliente.cuentas:
                cuentas_list.selection_set(0)
            refresh_historial()
            refresh_resumen()

        def pedir_monto(titulo):
            return simpledialog.askfloat(titulo, "Monto:", minvalue=0.01, parent=self)

        def depositar():
            cuenta = cuenta_seleccionada()
            if cuenta is None:
                return
            monto = pedir_monto("Depositar")
            if monto is None:
                return
            try:
                self.cajera.realizar_deposito(cuenta, monto)
            except (BancoError, ValueError) as exc:
                self._mostrar_error(exc)
            refresh_cuentas()

        def extraer():
            cuenta = cuenta_seleccionada()
            if cuenta is None:
                return
            monto = pedir_monto("Extraer")
            if monto is None:
                return
            try:
                self.cajera.realizar_extraccion(cuenta, monto)
            except (BancoError, ValueError) as exc:
                self._mostrar_error(exc)
            refresh_cuentas()

        def transferir():
            origen = cuenta_seleccionada()
            if origen is None:
                return
            numero_destino = simpledialog.askstring(
                "Transferir", "Numero de cuenta destino:", parent=self
            )
            if not numero_destino:
                return
            destino = self._obtener_cuenta_por_numero(numero_destino.strip())
            if destino is None:
                self._mostrar_error(ValueError("La cuenta destino no existe."))
                return
            monto = pedir_monto("Transferir")
            if monto is None:
                return
            try:
                self.banco.transferir(origen, destino, monto)
            except (BancoError, ValueError) as exc:
                self._mostrar_error(exc)
            refresh_cuentas()

        def pagar_debito():
            cuenta = cuenta_seleccionada()
            debitos = [t for t in cliente.tarjetas if isinstance(t, TarjetaDebito) and t.cuenta is cuenta]
            if not debitos:
                self._mostrar_error(ValueError("No hay tarjeta de debito para esta cuenta."))
                return
            monto = pedir_monto("Pago con debito")
            if monto is None:
                return
            try:
                debitos[0].pagar(monto, "Pago con debito en UI")
            except (BancoError, ValueError) as exc:
                self._mostrar_error(exc)
            refresh_cuentas()

        def pagar_credito():
            tarjetas = [t for t in cliente.tarjetas if isinstance(t, TarjetaCredito)]
            if not tarjetas:
                self._mostrar_error(ValueError("No tenes tarjeta de credito."))
                return
            monto = pedir_monto("Compra con credito")
            if monto is None:
                return
            try:
                tarjetas[0].pagar_con_tarjeta(monto, "Compra UI")
            except (BancoError, ValueError) as exc:
                self._mostrar_error(exc)
            refresh_resumen()

        def pagar_deuda_credito():
            cuenta = cuenta_seleccionada()
            tarjetas = [t for t in cliente.tarjetas if isinstance(t, TarjetaCredito)]
            if not tarjetas:
                self._mostrar_error(ValueError("No tenes tarjeta de credito."))
                return
            monto = pedir_monto("Pagar deuda TC")
            if monto is None:
                return
            try:
                tarjetas[0].pagar_deuda(monto, cuenta)
            except (BancoError, ValueError) as exc:
                self._mostrar_error(exc)
            refresh_cuentas()

        def pedir_prestamo():
            cuenta = cuenta_seleccionada()
            if cuenta is None:
                return
            monto = pedir_monto("Solicitar prestamo")
            if monto is None:
                return
            cuotas = simpledialog.askinteger("Solicitar prestamo", "Cantidad de cuotas:", minvalue=1, parent=self)
            if cuotas is None:
                return
            self.asesor.tramitar_prestamo(cliente, monto, 0.03, cuotas, cuenta)
            messagebox.showinfo("Prestamo", "Prestamo enviado para aprobacion del gerente.")
            refresh_resumen()

        def crear_inversion():
            cuenta = cuenta_seleccionada()
            if cuenta is None:
                return
            monto = pedir_monto("Crear inversion")
            if monto is None:
                return
            meses = simpledialog.askinteger("Crear inversion", "Meses:", minvalue=1, parent=self)
            if meses is None:
                return
            try:
                inv = self.asesor.crear_inversion(cliente, monto, 0.60, meses, cuenta)
                if inv is None:
                    self._mostrar_error(BancoError("No se pudo crear la inversion."))
            except (BancoError, ValueError) as exc:
                self._mostrar_error(exc)
            refresh_cuentas()

        tk.Button(botones, text="Depositar", font=FONT_SMALL, bg=ML_GREEN, fg=ML_WHITE, relief="flat", command=depositar).pack(side="left", padx=3)
        tk.Button(botones, text="Extraer", font=FONT_SMALL, bg=ML_RED, fg=ML_WHITE, relief="flat", command=extraer).pack(side="left", padx=3)
        tk.Button(botones, text="Transferir", font=FONT_SMALL, bg=ML_BLUE, fg=ML_WHITE, relief="flat", command=transferir).pack(side="left", padx=3)

        tk.Label(right, text="Tarjetas", font=FONT_BOLD, bg=ML_WHITE, fg=ML_DARK).pack(anchor="w", padx=12, pady=(10, 4))
        tk.Button(right, text="Pagar con debito", font=FONT_SMALL, bg=ML_YELLOW, fg=ML_WHITE, relief="flat", command=pagar_debito).pack(fill="x", padx=12, pady=2)
        tk.Button(right, text="Compra con credito", font=FONT_SMALL, bg=ML_YELLOW, fg=ML_WHITE, relief="flat", command=pagar_credito).pack(fill="x", padx=12, pady=2)
        tk.Button(right, text="Pagar deuda TC", font=FONT_SMALL, bg=ML_LIGHT, fg=ML_DARK, relief="flat", command=pagar_deuda_credito).pack(fill="x", padx=12, pady=2)

        tk.Label(right, text="Productos bancarios", font=FONT_BOLD, bg=ML_WHITE, fg=ML_DARK).pack(anchor="w", padx=12, pady=(14, 4))
        tk.Button(right, text="Solicitar prestamo", font=FONT_SMALL, bg=ML_BLUE, fg=ML_WHITE, relief="flat", command=pedir_prestamo).pack(fill="x", padx=12, pady=2)
        tk.Button(right, text="Crear inversion", font=FONT_SMALL, bg=ML_BLUE, fg=ML_WHITE, relief="flat", command=crear_inversion).pack(fill="x", padx=12, pady=2)

        cuentas_list.bind("<<ListboxSelect>>", refresh_historial)
        refresh_cuentas()

    def show_admin(self):
        clear(self.main_frame)
        gerente = self.usuario_actual["obj"]
        self._make_header(f"Panel de administracion - {gerente.nombre}")

        body = tk.Frame(self.main_frame, bg=ML_BG)
        body.pack(fill="both", expand=True, padx=20, pady=12)

        left = tk.Frame(body, bg=ML_WHITE, width=290)
        left.pack(side="left", fill="y", padx=(0, 10), pady=4)
        left.pack_propagate(False)

        right = tk.Frame(body, bg=ML_WHITE)
        right.pack(side="right", fill="both", expand=True, pady=4)

        tk.Label(left, text="Clientes", font=FONT_BOLD, bg=ML_WHITE, fg=ML_DARK).pack(pady=(12, 6))

        clientes_list = tk.Listbox(left, font=FONT_LABEL, relief="solid", bd=1)
        clientes_list.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        detalle = tk.Text(right, font=FONT_SMALL, relief="solid", bd=1, height=16)
        detalle.pack(fill="both", expand=True, padx=12, pady=(12, 8))

        acciones = tk.Frame(right, bg=ML_WHITE)
        acciones.pack(fill="x", padx=12, pady=(0, 12))

        def cliente_seleccionado():
            sel = clientes_list.curselection()
            if not sel:
                return None
            return self.clientes[sel[0]]

        def pedir_cuenta(cliente, titulo):
            if not cliente.cuentas:
                self._mostrar_error(ValueError("El cliente no tiene cuentas."))
                return None
            if len(cliente.cuentas) == 1:
                return cliente.cuentas[0]
            numero = simpledialog.askstring(titulo, "Numero de cuenta:", parent=self)
            if not numero:
                return None
            cuenta = self._obtener_cuenta_por_numero(numero.strip())
            if cuenta not in cliente.cuentas:
                self._mostrar_error(ValueError("Cuenta invalida para ese cliente."))
                return None
            return cuenta

        def refresh_clientes():
            clientes_list.delete(0, "end")
            for c in self.clientes:
                clientes_list.insert("end", f"{c.nombre} - DNI {c.get_dni()}")
            if self.clientes:
                clientes_list.selection_set(0)
            refresh_detalle()

        def refresh_detalle(*_):
            cliente = cliente_seleccionado()
            detalle.config(state="normal")
            detalle.delete("1.0", "end")
            if cliente is None:
                detalle.insert("end", "Selecciona un cliente.")
                detalle.config(state="disabled")
                return

            detalle.insert("end", f"Cliente: {cliente.nombre}\n")
            detalle.insert("end", f"DNI: {cliente.get_dni()}\n")
            detalle.insert("end", f"Email: {cliente.email}\n\n")

            detalle.insert("end", "Cuentas:\n")
            if cliente.cuentas:
                for c in cliente.cuentas:
                    detalle.insert("end", f"  - #{c.numero} ({c.__class__.__name__}) Saldo ${c.get_saldo():.2f}\n")
            else:
                detalle.insert("end", "  - Sin cuentas\n")

            detalle.insert("end", "\nPrestamos:\n")
            if cliente.prestamos:
                for p in cliente.prestamos:
                    estado = "APROBADO" if p.aprobado else "PENDIENTE"
                    detalle.insert("end", f"  - ${p.monto:.2f} | {estado}\n")
            else:
                detalle.insert("end", "  - Sin prestamos\n")

            detalle.config(state="disabled")

        def registrar_cliente():
            nombre = simpledialog.askstring("Nuevo cliente", "Nombre:", parent=self)
            if not nombre:
                return
            dni = simpledialog.askstring("Nuevo cliente", "DNI:", parent=self)
            if not dni:
                return
            email = simpledialog.askstring("Nuevo cliente", "Email:", parent=self)
            if not email:
                return
            cliente = self.banco.registrar_cliente(nombre.strip(), dni.strip(), email.strip(), self.sucursal)
            self.clientes.append(cliente)
            refresh_clientes()

        def abrir_caja():
            cliente = cliente_seleccionado()
            if cliente is None:
                return
            self.asesor.abrir_caja_ahorro(self.banco, cliente)
            refresh_detalle()

        def abrir_corriente():
            cliente = cliente_seleccionado()
            if cliente is None:
                return
            limite = simpledialog.askfloat("Cuenta corriente", "Limite descubierto:", minvalue=0.0, parent=self)
            if limite is None:
                return
            self.asesor.abrir_cuenta_corriente(self.banco, cliente, limite)
            refresh_detalle()

        def depositar_cliente():
            cliente = cliente_seleccionado()
            if cliente is None:
                return
            cuenta = pedir_cuenta(cliente, "Depositar")
            if cuenta is None:
                return
            monto = simpledialog.askfloat("Depositar", "Monto:", minvalue=0.01, parent=self)
            if monto is None:
                return
            try:
                self.cajera.realizar_deposito(cuenta, monto)
            except (BancoError, ValueError) as exc:
                self._mostrar_error(exc)
            refresh_detalle()

        def extraer_cliente():
            cliente = cliente_seleccionado()
            if cliente is None:
                return
            cuenta = pedir_cuenta(cliente, "Extraer")
            if cuenta is None:
                return
            monto = simpledialog.askfloat("Extraer", "Monto:", minvalue=0.01, parent=self)
            if monto is None:
                return
            try:
                self.cajera.realizar_extraccion(cuenta, monto)
            except (BancoError, ValueError) as exc:
                self._mostrar_error(exc)
            refresh_detalle()

        def aprobar_prestamo_pendiente():
            for cliente in self.clientes:
                for prestamo in cliente.prestamos:
                    if not prestamo.aprobado:
                        self.gerente.aprobar_prestamo(prestamo)
                        messagebox.showinfo("Prestamo", f"Prestamo de {cliente.nombre} aprobado.")
                        refresh_detalle()
                        return
            messagebox.showinfo("Prestamo", "No hay prestamos pendientes.")

        def crear_prestamo():
            cliente = cliente_seleccionado()
            if cliente is None:
                return
            cuenta = pedir_cuenta(cliente, "Prestamo")
            if cuenta is None:
                return
            monto = simpledialog.askfloat("Prestamo", "Monto:", minvalue=0.01, parent=self)
            if monto is None:
                return
            cuotas = simpledialog.askinteger("Prestamo", "Cuotas:", minvalue=1, parent=self)
            if cuotas is None:
                return
            self.asesor.tramitar_prestamo(cliente, monto, 0.03, cuotas, cuenta)
            refresh_detalle()

        tk.Button(acciones, text="Registrar cliente", font=FONT_SMALL, bg=ML_YELLOW, fg=ML_WHITE, relief="flat", command=registrar_cliente).pack(side="left", padx=3)
        tk.Button(acciones, text="Abrir caja ahorro", font=FONT_SMALL, bg=ML_GREEN, fg=ML_WHITE, relief="flat", command=abrir_caja).pack(side="left", padx=3)
        tk.Button(acciones, text="Abrir cta corriente", font=FONT_SMALL, bg=ML_GREEN, fg=ML_WHITE, relief="flat", command=abrir_corriente).pack(side="left", padx=3)

        acciones2 = tk.Frame(right, bg=ML_WHITE)
        acciones2.pack(fill="x", padx=12, pady=(0, 12))

        tk.Button(acciones2, text="Depositar", font=FONT_SMALL, bg=ML_YELLOW, fg=ML_DARK, relief="flat", command=depositar_cliente).pack(side="left", padx=3)
        tk.Button(acciones2, text="Extraer", font=FONT_SMALL, bg=ML_RED, fg=ML_WHITE, relief="flat", command=extraer_cliente).pack(side="left", padx=3)
        tk.Button(acciones2, text="Crear prestamo", font=FONT_SMALL, bg=ML_YELLOW, fg=ML_WHITE, relief="flat", command=crear_prestamo).pack(side="left", padx=3)
        tk.Button(acciones2, text="Aprobar pendientes", font=FONT_SMALL, bg=ML_DARK, fg=ML_WHITE, relief="flat", command=aprobar_prestamo_pendiente).pack(side="left", padx=3)

        clientes_list.bind("<<ListboxSelect>>", refresh_detalle)
        refresh_clientes()


if __name__ == "__main__":
    BancoApp().mainloop()
