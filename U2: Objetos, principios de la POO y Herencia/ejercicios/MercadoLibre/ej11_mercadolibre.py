# ── BACKEND ──────────────────────────────────────────────────────────────────
# Las clases las escriben los alumnos en ej11_clases.py

from ej11_clases import Producto, Usuario, Cliente, Admin, Tienda, App


# ── DATOS DE PRUEBA ───────────────────────────────────────────────────────────

tienda = Tienda()
app = App(tienda)

tienda.agregar_producto(Producto("Notebook Lenovo", 1200.00))
tienda.agregar_producto(Producto("Mouse inalámbrico", 45.00))
tienda.agregar_producto(Producto("Teclado mecánico", 89.99))
tienda.agregar_producto(Producto("Monitor 24\"", 350.00))

cliente1 = Cliente("Facundo", "facundo@mail.com", "1234")
tienda.registrar_usuario(cliente1)

admin1 = Admin("Admin", "admin@mail.com", "admin123", tienda)
tienda.registrar_usuario(admin1)


# ── UI ────────────────────────────────────────────────────────────────────────

import tkinter as tk
from tkinter import messagebox, simpledialog

ML_YELLOW = "#FFE600"
ML_BLUE   = "#3483FA"
ML_BG     = "#EBEBEB"
ML_WHITE  = "#FFFFFF"
ML_DARK   = "#333333"
ML_LIGHT  = "#F5F5F5"
ML_RED    = "#E53935"
ML_GREEN  = "#2E7D32"

FONT_TITLE  = ("Arial", 18, "bold")
FONT_LABEL  = ("Arial", 11)
FONT_BOLD   = ("Arial", 11, "bold")
FONT_SMALL  = ("Arial", 9)
FONT_BUTTON = ("Arial", 10, "bold")


def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()


class MLApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MercadoLibre — Simulador")
        self.geometry("700x520")
        self.resizable(False, False)
        self.configure(bg=ML_BG)
        self.usuario_actual = None

        self.main_frame = tk.Frame(self, bg=ML_BG)
        self.main_frame.pack(fill="both", expand=True)

        self.show_login()

    # ── LOGIN ─────────────────────────────────────────────────────────────────

    def show_login(self):
        clear(self.main_frame)
        self.usuario_actual = None

        # Header
        header = tk.Frame(self.main_frame, bg=ML_YELLOW, height=70)
        header.pack(fill="x")
        tk.Label(header, text="mercadolibre", font=("Arial", 22, "bold"),
                 bg=ML_YELLOW, fg=ML_DARK).pack(pady=15)

        # Card
        card = tk.Frame(self.main_frame, bg=ML_WHITE, padx=40, pady=30,
                        relief="flat", bd=0)
        card.pack(pady=40, ipadx=20, ipady=10)

        tk.Label(card, text="Iniciá sesión", font=FONT_TITLE,
                 bg=ML_WHITE, fg=ML_DARK).grid(row=0, column=0, columnspan=2,
                                               pady=(0, 20))

        tk.Label(card, text="Email", font=FONT_LABEL,
                 bg=ML_WHITE, fg=ML_DARK).grid(row=1, column=0, sticky="w")
        email_entry = tk.Entry(card, font=FONT_LABEL, width=28,
                               relief="solid", bd=1)
        email_entry.grid(row=2, column=0, pady=(4, 14), ipady=6)

        tk.Label(card, text="Contraseña", font=FONT_LABEL,
                 bg=ML_WHITE, fg=ML_DARK).grid(row=3, column=0, sticky="w")
        pass_entry = tk.Entry(card, font=FONT_LABEL, width=28, show="•",
                              relief="solid", bd=1)
        pass_entry.grid(row=4, column=0, pady=(4, 20), ipady=6)

        def do_login():
            usuario = app.login(email_entry.get(), pass_entry.get())
            if usuario:
                self.usuario_actual = usuario
                if isinstance(usuario, Admin):
                    self.show_admin()
                else:
                    self.show_cliente()
            else:
                messagebox.showerror("Error", "Email o contraseña incorrectos")

        tk.Button(card, text="Ingresar", font=FONT_BUTTON,
                  bg=ML_BLUE, fg=ML_WHITE, relief="flat",
                  cursor="hand2", width=24, pady=8,
                  command=do_login).grid(row=5, column=0, pady=(0, 6))

        # Hint
        hint = tk.Label(self.main_frame,
                        text="Cliente: facundo@mail.com / 1234    |    Admin: admin@mail.com / admin123",
                        font=FONT_SMALL, bg=ML_BG, fg="#888888")
        hint.pack()

    # ── HEADER compartido ─────────────────────────────────────────────────────

    def _make_header(self, subtitulo):
        header = tk.Frame(self.main_frame, bg=ML_YELLOW, height=60)
        header.pack(fill="x")
        tk.Label(header, text="mercadolibre", font=("Arial", 16, "bold"),
                 bg=ML_YELLOW, fg=ML_DARK).pack(side="left", padx=16, pady=12)
        tk.Label(header, text=subtitulo, font=FONT_LABEL,
                 bg=ML_YELLOW, fg=ML_DARK).pack(side="left")
        tk.Button(header, text="Cerrar sesión", font=FONT_SMALL,
                  bg=ML_DARK, fg=ML_WHITE, relief="flat", cursor="hand2",
                  command=self.show_login).pack(side="right", padx=16, pady=14)

    # ── VISTA CLIENTE ─────────────────────────────────────────────────────────

    def show_cliente(self):
        clear(self.main_frame)
        u = self.usuario_actual
        self._make_header(f"Hola, {u.nombre}")

        body = tk.Frame(self.main_frame, bg=ML_BG)
        body.pack(fill="both", expand=True, padx=20, pady=12)

        # ── Columna izquierda: productos ──────────────────────────────────────
        left = tk.Frame(body, bg=ML_WHITE, relief="flat", bd=0)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=4)

        tk.Label(left, text="Productos disponibles", font=FONT_BOLD,
                 bg=ML_WHITE, fg=ML_DARK).pack(pady=(12, 6))

        prod_frame = tk.Frame(left, bg=ML_WHITE)
        prod_frame.pack(fill="both", expand=True, padx=10)

        def refresh_productos():
            clear(prod_frame)
            for prod in tienda.mostrar_productos():
                row = tk.Frame(prod_frame, bg=ML_LIGHT, pady=6, padx=10)
                row.pack(fill="x", pady=3)
                tk.Label(row, text=str(prod), font=FONT_LABEL,
                         bg=ML_LIGHT, fg=ML_DARK).pack(side="left")
                tk.Button(row, text="Agregar al carrito",
                          font=FONT_SMALL, bg=ML_YELLOW, fg=ML_DARK,
                          relief="flat", cursor="hand2",
                          command=lambda p=prod: agregar(p)).pack(side="right")

        def agregar(prod):
            u.agregar_producto_al_carrito(prod)
            refresh_carrito()
            lbl_total.config(text=f"Total: ${u.total_carrito():.2f}")

        refresh_productos()

        # ── Columna derecha: carrito ──────────────────────────────────────────
        right = tk.Frame(body, bg=ML_WHITE, width=220, relief="flat", bd=0)
        right.pack(side="right", fill="y", pady=4)
        right.pack_propagate(False)

        tk.Label(right, text="Mi carrito", font=FONT_BOLD,
                 bg=ML_WHITE, fg=ML_DARK).pack(pady=(12, 6))

        carrito_frame = tk.Frame(right, bg=ML_WHITE)
        carrito_frame.pack(fill="both", expand=True, padx=10)

        lbl_total = tk.Label(right, text="Total: $0.00", font=FONT_BOLD,
                             bg=ML_WHITE, fg=ML_BLUE)
        lbl_total.pack(pady=6)

        def refresh_carrito():
            clear(carrito_frame)
            if not u.carrito:
                tk.Label(carrito_frame, text="El carrito está vacío",
                         font=FONT_SMALL, bg=ML_WHITE, fg="#888").pack(pady=10)
                return
            for item in u.carrito:
                tk.Label(carrito_frame, text=f"• {item.nombre}  ${item.precio:.2f}",
                         font=FONT_SMALL, bg=ML_WHITE,
                         fg=ML_DARK, anchor="w").pack(fill="x")

        def vaciar():
            u.vaciar_carrito()
            refresh_carrito()
            lbl_total.config(text="Total: $0.00")

        tk.Button(right, text="Vaciar carrito", font=FONT_SMALL,
                  bg=ML_RED, fg=ML_WHITE, relief="flat", cursor="hand2",
                  command=vaciar).pack(pady=(0, 8))

        tk.Button(right, text="Comprar  ✓", font=FONT_BUTTON,
                  bg=ML_GREEN, fg=ML_WHITE, relief="flat", cursor="hand2",
                  command=lambda: (messagebox.showinfo(
                      "Compra exitosa",
                      f"Compraste {len(u.carrito)} producto(s) por ${u.total_carrito():.2f}"),
                      vaciar())).pack(pady=(0, 12))

        refresh_carrito()

    # ── VISTA ADMIN ───────────────────────────────────────────────────────────

    def show_admin(self):
        clear(self.main_frame)
        u = self.usuario_actual
        self._make_header(f"Panel de Admin — {u.nombre}")

        body = tk.Frame(self.main_frame, bg=ML_BG)
        body.pack(fill="both", expand=True, padx=20, pady=12)

        # ── Lista de productos ────────────────────────────────────────────────
        card = tk.Frame(body, bg=ML_WHITE)
        card.pack(fill="both", expand=True, pady=(0, 10))

        tk.Label(card, text="Productos en la tienda", font=FONT_BOLD,
                 bg=ML_WHITE, fg=ML_DARK).pack(pady=(12, 6))

        list_frame = tk.Frame(card, bg=ML_WHITE)
        list_frame.pack(fill="both", expand=True, padx=16)

        def refresh():
            clear(list_frame)
            if not tienda.lista_productos:
                tk.Label(list_frame, text="No hay productos cargados.",
                         font=FONT_SMALL, bg=ML_WHITE, fg="#888").pack(pady=10)
                return
            for prod in tienda.lista_productos:
                row = tk.Frame(list_frame, bg=ML_LIGHT, pady=6, padx=10)
                row.pack(fill="x", pady=3)
                tk.Label(row, text=str(prod), font=FONT_LABEL,
                         bg=ML_LIGHT, fg=ML_DARK).pack(side="left")
                tk.Button(row, text="Eliminar", font=FONT_SMALL,
                          bg=ML_RED, fg=ML_WHITE, relief="flat", cursor="hand2",
                          command=lambda p=prod: eliminar(p)).pack(side="right")

        def eliminar(prod):
            if messagebox.askyesno("Confirmar", f"¿Eliminar '{prod.nombre}'?"):
                u.eliminar_producto(prod)
                refresh()

        refresh()

        # ── Formulario nuevo producto ─────────────────────────────────────────
        form = tk.Frame(body, bg=ML_WHITE, padx=20, pady=14)
        form.pack(fill="x")

        tk.Label(form, text="Agregar producto", font=FONT_BOLD,
                 bg=ML_WHITE, fg=ML_DARK).grid(row=0, column=0,
                                               columnspan=4, sticky="w",
                                               pady=(0, 10))

        tk.Label(form, text="Nombre", font=FONT_LABEL,
                 bg=ML_WHITE).grid(row=1, column=0, sticky="w")
        nombre_entry = tk.Entry(form, font=FONT_LABEL, width=22,
                                relief="solid", bd=1)
        nombre_entry.grid(row=1, column=1, padx=(6, 20), ipady=5)

        tk.Label(form, text="Precio", font=FONT_LABEL,
                 bg=ML_WHITE).grid(row=1, column=2, sticky="w")
        precio_entry = tk.Entry(form, font=FONT_LABEL, width=10,
                                relief="solid", bd=1)
        precio_entry.grid(row=1, column=3, padx=(6, 20), ipady=5)

        def crear():
            nombre = nombre_entry.get().strip()
            try:
                precio = float(precio_entry.get())
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número")
                return
            if not nombre:
                messagebox.showerror("Error", "El nombre no puede estar vacío")
                return
            u.crear_producto(nombre, precio)
            nombre_entry.delete(0, "end")
            precio_entry.delete(0, "end")
            refresh()

        tk.Button(form, text="Crear producto", font=FONT_BUTTON,
                  bg=ML_BLUE, fg=ML_WHITE, relief="flat", cursor="hand2",
                  pady=6, command=crear).grid(row=1, column=4, padx=(0, 0))


if __name__ == "__main__":
    MLApp().mainloop()
