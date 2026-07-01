# Ejercicios Integradores: Herencia + Composición + Asociación

> Cada ejercicio pide **5 o 6 clases** e integra los tres tipos de relaciones vistos en la teoría (secciones 10 a 14).
> Cada clase debe tener aproximadamente **3 métodos** (más si es necesario para que sean útiles).
> No es obligatorio usar decoradores.

---

## Ejercicio 1 — Hospital

Modelar un sistema de gestión hospitalaria con personas, médicos, pacientes y consultas.

### Clase `Persona`

| Tipo      | Nombre              | Descripción                                        |
|-----------|---------------------|----------------------------------------------------|
| Atributo  | `nombre`            | Cómo se llama.                                     |
| Atributo  | `dni`               | Documento identificatorio.                         |
| Atributo  | `edad`              | Años que tiene.                                    |
| Método    | `mostrar_datos()`   | Muestra su información básica.                     |
| Método    | `es_mayor_de_edad()`| Indica si supera cierto umbral.                    |
| Método    | `saludar()`         | Realiza una acción de presentación.                |

### Clase `Paciente(Persona)`

| Tipo      | Nombre                       | Descripción                                       |
|-----------|------------------------------|---------------------------------------------------|
| Atributo  | `historia_clinica`           | Registro acumulado del paciente.                  |
| Atributo  | `obra_social`                | Cobertura médica (puede no tener).                |
| Método    | `agregar_diagnostico(texto)` | Suma un ítem a su registro.                       |
| Método    | `mostrar_historia()`         | Muestra el registro completo.                     |
| Método    | `tiene_obra_social()`        | Indica si cuenta con cobertura.                   |
| Método    | `mostrar_datos()`            | Extiende la información básica.                   |

### Clase `Medico(Persona)`

| Tipo      | Nombre                             | Descripción                                 |
|-----------|------------------------------------|---------------------------------------------|
| Atributo  | `especialidad`                     | Área en la que trabaja.                     |
| Atributo  | `matricula`                        | Identificador profesional.                  |
| Método    | `atender(paciente, diagnostico)`   | Realiza una acción sobre un paciente.       |
| Método    | `mostrar_especialidad()`           | Informa su área.                            |
| Método    | `cambiar_especialidad(nueva)`      | Actualiza su área.                          |

### Clase `Consulta`

| Tipo      | Nombre                | Descripción                                              |
|-----------|-----------------------|----------------------------------------------------------|
| Atributo  | `medico`              | Profesional involucrado (referencia externa).            |
| Atributo  | `paciente`            | Persona atendida (referencia externa).                   |
| Atributo  | `fecha`               | Cuándo ocurre.                                           |
| Atributo  | `motivo`              | Por qué se realiza.                                      |
| Método    | `realizar()`          | Concreta el encuentro y afecta al paciente.              |
| Método    | `resumen()`           | Devuelve una descripción resumida.                       |
| Método    | `cambiar_fecha(nueva)`| Modifica el momento.                                     |

### Clase `Hospital`

| Tipo      | Nombre                                     | Descripción                                    |
|-----------|--------------------------------------------|------------------------------------------------|
| Atributo  | `nombre`                                   | Denominación del hospital.                     |
| Atributo  | `medicos`                                  | Conjunto de profesionales propios.             |
| Atributo  | `consultas`                                | Registro de encuentros.                        |
| Método    | `contratar_medico(medico)`                 | Suma un profesional.                           |
| Método    | `registrar_consulta(consulta)`             | Deja constancia de un encuentro.               |
| Método    | `listar_consultas()`                       | Muestra todos los encuentros registrados.      |
| Método    | `medicos_por_especialidad(especialidad)`   | Filtra profesionales según un criterio.        |

---

## Ejercicio 2 — Aerolínea

Modelar una aerolínea con vuelos, pasajeros, tripulación y aviones.

### Clase `Persona`

| Tipo      | Nombre                | Descripción                                |
|-----------|-----------------------|--------------------------------------------|
| Atributo  | `nombre`              | Cómo se llama.                             |
| Atributo  | `dni`                 | Documento identificatorio.                 |
| Método    | `mostrar_datos()`     | Muestra su información básica.             |
| Método    | `cambiar_nombre(nuevo)`| Actualiza cómo se llama.                  |
| Método    | `__str__()`           | Representación como texto.                 |

### Clase `Pasajero(Persona)`

| Tipo      | Nombre                     | Descripción                                    |
|-----------|----------------------------|------------------------------------------------|
| Atributo  | `numero_pasaporte`         | Identificación para viajar.                    |
| Atributo  | `millas_acumuladas`        | Beneficio acumulado por viajes.                |
| Método    | `sumar_millas(cantidad)`   | Incrementa el beneficio acumulado.             |
| Método    | `es_frecuente()`           | Indica si supera cierto umbral.                |
| Método    | `mostrar_datos()`          | Extiende la información básica.                |

### Clase `Tripulante(Persona)`

| Tipo      | Nombre               | Descripción                                    |
|-----------|----------------------|------------------------------------------------|
| Atributo  | `rol`                | Función que cumple (piloto, azafata, etc.).    |
| Atributo  | `licencia`           | Habilitación profesional.                      |
| Método    | `presentarse()`      | Informa su función.                            |
| Método    | `cambiar_rol(nuevo)` | Actualiza su función.                          |
| Método    | `mostrar_datos()`    | Extiende la información básica.                |

### Clase `Avion`

| Tipo      | Nombre                            | Descripción                                  |
|-----------|-----------------------------------|----------------------------------------------|
| Atributo  | `matricula`                       | Identificación de la aeronave.               |
| Atributo  | `modelo`                          | Tipo de aeronave.                            |
| Atributo  | `capacidad`                       | Cantidad máxima que puede transportar.       |
| Método    | `info()`                          | Muestra datos generales.                     |
| Método    | `puede_llevar(cantidad_pasajeros)`| Verifica si entra cierta cantidad.           |
| Método    | `cambiar_modelo(nuevo)`           | Actualiza su tipo.                           |

### Clase `Vuelo`

| Tipo      | Nombre                              | Descripción                                     |
|-----------|-------------------------------------|-------------------------------------------------|
| Atributo  | `numero_vuelo`                      | Identificación única.                           |
| Atributo  | `origen`                            | Desde dónde parte.                              |
| Atributo  | `destino`                           | A dónde llega.                                  |
| Atributo  | `avion`                             | Aeronave asignada.                              |
| Atributo  | `tripulantes`                       | Personal a bordo (referencias externas).        |
| Atributo  | `pasajeros`                         | Viajeros a bordo (referencias externas).        |
| Método    | `agregar_pasajero(p)`               | Suma un viajero.                                |
| Método    | `agregar_tripulante(t)`             | Suma personal a bordo.                          |
| Método    | `mostrar_manifiesto()`              | Muestra todos los que viajan.                   |
| Método    | `sumar_millas_a_pasajeros(millas)`  | Beneficia a todos los viajeros.                 |

### Clase `Aerolinea`

| Tipo      | Nombre                       | Descripción                                     |
|-----------|------------------------------|-------------------------------------------------|
| Atributo  | `nombre`                     | Denominación de la empresa.                     |
| Atributo  | `aviones`                    | Flota propia.                                   |
| Atributo  | `vuelos`                     | Vuelos programados.                             |
| Método    | `programar_vuelo(vuelo)`     | Suma un vuelo al calendario.                    |
| Método    | `listar_vuelos()`            | Muestra todos los programados.                  |
| Método    | `vuelos_a_destino(destino)`  | Filtra según un criterio de llegada.            |

---

## Ejercicio 3 — Streaming de música

Modelar una plataforma tipo Spotify.

### Clase `Usuario`

| Tipo      | Nombre                | Descripción                              |
|-----------|-----------------------|------------------------------------------|
| Atributo  | `nombre`              | Cómo se llama.                           |
| Atributo  | `email`               | Contacto electrónico.                    |
| Atributo  | `edad`                | Años que tiene.                          |
| Método    | `mostrar_datos()`     | Muestra su información.                  |
| Método    | `es_mayor_de_edad()`  | Indica si supera cierto umbral.          |
| Método    | `cambiar_email(nuevo)`| Actualiza el contacto.                   |

### Clase `Cancion`

| Tipo      | Nombre                   | Descripción                              |
|-----------|--------------------------|------------------------------------------|
| Atributo  | `titulo`                 | Cómo se llama la pista.                  |
| Atributo  | `artista`                | Quién la interpreta.                     |
| Atributo  | `duracion`               | Longitud (en segundos).                  |
| Método    | `reproducir()`           | Simula la acción de escucharla.          |
| Método    | `duracion_formateada()`  | Devuelve la longitud en formato legible. |
| Método    | `info()`                 | Muestra los datos generales.             |

### Clase `Playlist`

| Tipo      | Nombre                | Descripción                                          |
|-----------|-----------------------|------------------------------------------------------|
| Atributo  | `nombre`              | Cómo se llama la lista.                              |
| Atributo  | `dueño`               | Quién la creó (referencia externa).                  |
| Atributo  | `canciones`           | Pistas incluidas (referencias externas).             |
| Método    | `agregar_cancion(c)`  | Suma una pista.                                      |
| Método    | `quitar_cancion(c)`   | Elimina una pista.                                   |
| Método    | `duracion_total()`    | Calcula cuánto dura toda la lista.                   |
| Método    | `reproducir_todas()`  | Recorre y ejecuta cada pista.                        |

### Clase `Suscripcion`

| Tipo      | Nombre                | Descripción                                       |
|-----------|-----------------------|---------------------------------------------------|
| Atributo  | `tipo`                | Nivel del plan (free / premium).                  |
| Atributo  | `precio`              | Cuánto cuesta.                                    |
| Atributo  | `usuario`             | A quién pertenece.                                |
| Método    | `es_premium()`        | Indica si es del nivel más alto.                  |
| Método    | `renovar()`           | Extiende su vigencia.                             |
| Método    | `cambiar_tipo(nuevo)` | Cambia de plan.                                   |

### Clase `PlataformaStreaming`

| Tipo      | Nombre                                | Descripción                                  |
|-----------|---------------------------------------|----------------------------------------------|
| Atributo  | `usuarios`                            | Registrados en el sistema.                   |
| Atributo  | `canciones`                           | Catálogo de pistas.                          |
| Atributo  | `playlists`                           | Listas creadas.                              |
| Método    | `registrar_usuario(u)`                | Suma un usuario.                             |
| Método    | `subir_cancion(c)`                    | Suma una pista al catálogo.                  |
| Método    | `crear_playlist(usuario, nombre)`     | Genera una lista para alguien.               |
| Método    | `buscar_canciones_por_artista(artista)`| Filtra el catálogo por intérprete.          |

---

## Ejercicio 4 — Escuela

Sistema de gestión escolar.

### Clase `Persona`

| Tipo      | Nombre                 | Descripción                              |
|-----------|------------------------|------------------------------------------|
| Atributo  | `nombre`               | Cómo se llama.                           |
| Atributo  | `dni`                  | Documento identificatorio.               |
| Método    | `mostrar_datos()`      | Muestra su información básica.           |
| Método    | `cambiar_nombre(nuevo)`| Actualiza cómo se llama.                 |
| Método    | `__str__()`            | Representación como texto.               |

### Clase `Estudiante(Persona)`

| Tipo      | Nombre                | Descripción                                    |
|-----------|-----------------------|------------------------------------------------|
| Atributo  | `grado`               | Año o nivel que cursa.                         |
| Atributo  | `notas`               | Calificaciones recibidas.                      |
| Método    | `agregar_nota(nota)`  | Suma una calificación.                         |
| Método    | `promedio()`          | Calcula el valor medio de sus calificaciones.  |
| Método    | `esta_aprobado()`     | Indica si supera cierto umbral.                |

### Clase `Docente(Persona)`

| Tipo      | Nombre                          | Descripción                                    |
|-----------|---------------------------------|------------------------------------------------|
| Atributo  | `materia`                       | Asignatura que dicta.                          |
| Atributo  | `antiguedad`                    | Años ejerciendo.                               |
| Método    | `tomar_examen(estudiante, nota)`| Registra una calificación en alguien.          |
| Método    | `mostrar_datos()`               | Extiende la información básica.                |
| Método    | `aumentar_antiguedad()`         | Suma un año.                                   |

### Clase `Aula`

| Tipo      | Nombre                  | Descripción                                       |
|-----------|-------------------------|---------------------------------------------------|
| Atributo  | `numero`                | Identificación física.                            |
| Atributo  | `capacidad`             | Cantidad máxima que admite.                       |
| Atributo  | `estudiantes`           | Quiénes están asignados.                          |
| Método    | `asignar_estudiante(e)` | Suma a alguien, respetando la capacidad.          |
| Método    | `esta_llena()`          | Indica si ya no entra nadie.                      |
| Método    | `listar_estudiantes()`  | Muestra quiénes están dentro.                     |

### Clase `Curso`

| Tipo      | Nombre                | Descripción                                            |
|-----------|-----------------------|--------------------------------------------------------|
| Atributo  | `nombre`              | Cómo se llama el curso.                                |
| Atributo  | `docente`             | Quién lo dicta (referencia externa).                   |
| Atributo  | `aula`                | Dónde se dicta (referencia externa).                   |
| Atributo  | `inscritos`           | Quiénes participan.                                    |
| Método    | `inscribir(estudiante)`| Suma a alguien al curso.                              |
| Método    | `dictar_clase()`      | Simula la actividad del curso.                         |
| Método    | `promedio_general()`  | Calcula un valor medio combinando a todos.             |

### Clase `Escuela`

| Tipo      | Nombre                                  | Descripción                                     |
|-----------|-----------------------------------------|-------------------------------------------------|
| Atributo  | `nombre`                                | Denominación del establecimiento.               |
| Atributo  | `aulas`                                 | Espacios físicos disponibles.                   |
| Atributo  | `cursos`                                | Actividades organizadas.                        |
| Método    | `crear_curso(docente, aula, nombre)`    | Genera y registra una nueva actividad.          |
| Método    | `listar_cursos()`                       | Muestra todas las actividades.                  |
| Método    | `estudiantes_aprobados()`               | Filtra según un criterio de rendimiento.        |

---

## Ejercicio 5 — E-commerce

Modelar una tienda online.

### Clase `Producto`

| Tipo      | Nombre                       | Descripción                                    |
|-----------|------------------------------|------------------------------------------------|
| Atributo  | `nombre`                     | Cómo se llama.                                 |
| Atributo  | `precio`                     | Cuánto cuesta la unidad.                       |
| Atributo  | `stock`                      | Cuántas unidades hay disponibles.              |
| Método    | `hay_stock(cantidad)`        | Indica si alcanza para algo pedido.            |
| Método    | `descontar_stock(cantidad)`  | Reduce la disponibilidad.                      |
| Método    | `info()`                     | Muestra los datos generales.                   |

### Clase `Cliente`

| Tipo      | Nombre                    | Descripción                              |
|-----------|---------------------------|------------------------------------------|
| Atributo  | `nombre`                  | Cómo se llama.                           |
| Atributo  | `email`                   | Contacto electrónico.                    |
| Atributo  | `direccion`               | Dónde recibe envíos.                     |
| Método    | `mostrar_datos()`         | Muestra su información.                  |
| Método    | `cambiar_direccion(nueva)`| Actualiza el destino de envío.           |
| Método    | `__str__()`               | Representación como texto.               |

### Clase `ItemCarrito`

| Tipo      | Nombre                  | Descripción                                       |
|-----------|-------------------------|---------------------------------------------------|
| Atributo  | `producto`              | Referencia al artículo.                           |
| Atributo  | `cantidad`              | Cuántas unidades incluye.                         |
| Método    | `subtotal()`            | Calcula el costo parcial del ítem.                |
| Método    | `aumentar_cantidad(n)`  | Suma más unidades del mismo artículo.             |
| Método    | `descripcion()`         | Muestra los datos del ítem.                       |

### Clase `Carrito`

| Tipo      | Nombre                                | Descripción                                    |
|-----------|---------------------------------------|------------------------------------------------|
| Atributo  | `cliente`                             | A quién pertenece.                             |
| Atributo  | `items`                               | Ítems que contiene.                            |
| Método    | `agregar_producto(producto, cantidad)`| Suma un artículo (o aumenta si ya está).       |
| Método    | `total()`                             | Calcula el costo global.                       |
| Método    | `vaciar()`                            | Elimina todos los ítems.                       |
| Método    | `mostrar_carrito()`                   | Muestra el contenido completo.                 |

### Clase `Pedido`

| Tipo      | Nombre        | Descripción                                              |
|-----------|---------------|----------------------------------------------------------|
| Atributo  | `cliente`     | Quién lo generó.                                         |
| Atributo  | `items`       | Copia de lo comprado al momento de la compra.            |
| Atributo  | `estado`      | Etapa en la que se encuentra (pendiente/pagado/enviado). |
| Método    | `pagar()`     | Avanza al siguiente estado.                              |
| Método    | `enviar()`    | Avanza al estado final.                                  |
| Método    | `resumen()`   | Muestra una descripción global.                          |

### Clase `Tienda`

| Tipo      | Nombre                        | Descripción                                    |
|-----------|-------------------------------|------------------------------------------------|
| Atributo  | `nombre`                      | Denominación del comercio.                     |
| Atributo  | `productos`                   | Catálogo disponible.                           |
| Atributo  | `pedidos`                     | Historial de operaciones.                      |
| Método    | `agregar_producto(p)`         | Suma un artículo al catálogo.                  |
| Método    | `registrar_pedido(pedido)`    | Deja constancia de una operación.              |
| Método    | `productos_sin_stock()`       | Filtra el catálogo por disponibilidad.         |
| Método    | `total_facturado()`           | Suma valores de todas las operaciones.         |

---

## Ejercicio 6 — Videojuego RPG

Modelar personajes y combate.

### Clase `Personaje`

| Tipo      | Nombre                | Descripción                                    |
|-----------|-----------------------|------------------------------------------------|
| Atributo  | `nombre`              | Cómo se llama.                                 |
| Atributo  | `hp`                  | Puntos de vida actuales.                       |
| Atributo  | `ataque`              | Cuánto daño base puede infligir.               |
| Método    | `recibir_dano(cantidad)`| Reduce los puntos de vida.                   |
| Método    | `esta_vivo()`         | Indica si aún puede seguir.                    |
| Método    | `atacar(otro)`        | Actúa sobre otro personaje.                    |

### Clase `Guerrero(Personaje)`

| Tipo      | Nombre                    | Descripción                                          |
|-----------|---------------------------|------------------------------------------------------|
| Atributo  | `defensa`                 | Reducción aplicada al daño recibido.                 |
| Método    | `recibir_dano(cantidad)`  | Aplica una versión diferente al comportamiento base. |
| Método    | `golpe_critico(otro)`     | Realiza un ataque más fuerte que el normal.          |
| Método    | `info()`                  | Muestra sus datos.                                   |

### Clase `Mago(Personaje)`

| Tipo      | Nombre                    | Descripción                                          |
|-----------|---------------------------|------------------------------------------------------|
| Atributo  | `mana`                    | Recurso necesario para acciones especiales.          |
| Método    | `lanzar_hechizo(otro)`    | Acción especial que consume el recurso.              |
| Método    | `recargar_mana(cantidad)` | Restaura el recurso.                                 |
| Método    | `info()`                  | Muestra sus datos.                                   |

### Clase `Arma`

| Tipo      | Nombre              | Descripción                                    |
|-----------|---------------------|------------------------------------------------|
| Atributo  | `nombre`            | Cómo se llama.                                 |
| Atributo  | `dano_extra`        | Cuánto suma al ataque base.                    |
| Método    | `info()`            | Muestra sus datos.                             |
| Método    | `mejorar(cantidad)` | Aumenta su valor de daño extra.                |
| Método    | `__str__()`         | Representación como texto.                     |

### Clase `Inventario`

| Tipo      | Nombre                | Descripción                                          |
|-----------|-----------------------|------------------------------------------------------|
| Atributo  | `dueño`               | A quién pertenece.                                   |
| Atributo  | `armas`               | Objetos que contiene.                                |
| Método    | `agregar_arma(a)`     | Suma un objeto.                                      |
| Método    | `quitar_arma(a)`      | Elimina un objeto.                                   |
| Método    | `mostrar_inventario()`| Muestra todo el contenido.                           |
| Método    | `arma_mas_fuerte()`   | Devuelve el objeto con mayor valor.                  |

### Clase `Batalla`

| Tipo      | Nombre                          | Descripción                                    |
|-----------|---------------------------------|------------------------------------------------|
| Atributo  | `personaje1`                    | Uno de los combatientes.                       |
| Atributo  | `personaje2`                    | El otro combatiente.                           |
| Método    | `iniciar()`                     | Ejecuta el combate hasta que termina.          |
| Método    | `turno(atacante, defensor)`     | Simula una acción entre dos partes.            |
| Método    | `ganador()`                     | Devuelve al que sobrevivió.                    |

---

## Ejercicio 7 — Restaurante

Sistema para gestionar un restaurante.

### Clase `Empleado`

| Tipo      | Nombre                       | Descripción                              |
|-----------|------------------------------|------------------------------------------|
| Atributo  | `nombre`                     | Cómo se llama.                           |
| Atributo  | `dni`                        | Documento identificatorio.               |
| Atributo  | `sueldo`                     | Cuánto cobra.                            |
| Método    | `mostrar_datos()`            | Muestra su información.                  |
| Método    | `aumentar_sueldo(porcentaje)`| Incrementa el sueldo en un porcentaje.   |
| Método    | `__str__()`                  | Representación como texto.               |

### Clase `Mozo(Empleado)`

| Tipo      | Nombre                        | Descripción                                    |
|-----------|-------------------------------|------------------------------------------------|
| Atributo  | `mesas_asignadas`             | Números de mesas que atiende.                  |
| Método    | `asignar_mesa(numero)`        | Suma una mesa a su zona.                       |
| Método    | `tomar_pedido(mesa, pedido)`  | Registra una orden en una mesa.                |
| Método    | `mostrar_datos()`             | Extiende la información básica.                |

### Clase `Cocinero(Empleado)`

| Tipo      | Nombre                        | Descripción                                    |
|-----------|-------------------------------|------------------------------------------------|
| Atributo  | `especialidad`                | Área de cocina en la que se destaca.           |
| Método    | `preparar(plato)`             | Ejecuta la elaboración de una comida.          |
| Método    | `cambiar_especialidad(nueva)` | Actualiza su área.                             |
| Método    | `mostrar_datos()`             | Extiende la información básica.                |

### Clase `Plato`

| Tipo      | Nombre                | Descripción                                       |
|-----------|-----------------------|---------------------------------------------------|
| Atributo  | `nombre`              | Cómo se llama la comida.                          |
| Atributo  | `precio`              | Cuánto cuesta.                                    |
| Atributo  | `ingredientes`        | De qué está compuesta.                            |
| Método    | `mostrar_ingredientes()`| Muestra la composición.                         |
| Método    | `info()`              | Muestra los datos generales.                      |
| Método    | `cambiar_precio(nuevo)`| Actualiza el costo.                              |

### Clase `Pedido`

| Tipo      | Nombre               | Descripción                                       |
|-----------|----------------------|---------------------------------------------------|
| Atributo  | `numero_mesa`        | Dónde se sirve.                                   |
| Atributo  | `mozo`               | Quién lo toma (referencia externa).               |
| Atributo  | `platos`             | Comidas incluidas.                                |
| Método    | `agregar_plato(p)`   | Suma una comida al pedido.                        |
| Método    | `total()`            | Calcula el costo global.                          |
| Método    | `cerrar_pedido()`    | Marca la orden como finalizada.                   |
| Método    | `resumen()`          | Muestra una descripción global.                   |

### Clase `Restaurante`

| Tipo      | Nombre                        | Descripción                                    |
|-----------|-------------------------------|------------------------------------------------|
| Atributo  | `nombre`                      | Denominación del local.                        |
| Atributo  | `empleados`                   | Personal contratado.                           |
| Atributo  | `menu`                        | Comidas disponibles.                           |
| Atributo  | `pedidos`                     | Historial de órdenes.                          |
| Método    | `contratar(empleado)`         | Suma personal.                                 |
| Método    | `agregar_plato_menu(p)`       | Suma una comida al menú.                       |
| Método    | `registrar_pedido(pedido)`    | Deja constancia de una orden.                  |
| Método    | `total_facturado()`           | Suma valores de todas las órdenes.             |

---

## Ejercicio 8 — Banco

Sistema bancario con distintos tipos de cuenta.

### Clase `Cliente`

| Tipo      | Nombre                | Descripción                              |
|-----------|-----------------------|------------------------------------------|
| Atributo  | `nombre`              | Cómo se llama.                           |
| Atributo  | `dni`                 | Documento identificatorio.               |
| Atributo  | `email`               | Contacto electrónico.                    |
| Método    | `mostrar_datos()`     | Muestra su información.                  |
| Método    | `cambiar_email(nuevo)`| Actualiza el contacto.                   |
| Método    | `__str__()`           | Representación como texto.               |

### Clase `Cuenta`

| Tipo      | Nombre                | Descripción                                       |
|-----------|-----------------------|---------------------------------------------------|
| Atributo  | `numero`              | Identificador de la cuenta.                       |
| Atributo  | `__saldo`             | Dinero disponible (acceso controlado).            |
| Atributo  | `cliente`             | A quién pertenece.                                |
| Método    | `depositar(monto)`    | Incrementa el dinero disponible.                  |
| Método    | `retirar(monto)`      | Reduce el dinero, validando factibilidad.         |
| Método    | `obtener_saldo()`     | Devuelve el dinero disponible.                    |

### Clase `CuentaCorriente(Cuenta)`

| Tipo      | Nombre                    | Descripción                                          |
|-----------|---------------------------|------------------------------------------------------|
| Atributo  | `limite_descubierto`      | Cuánto se puede retirar por debajo del saldo.        |
| Método    | `retirar(monto)`          | Aplica una versión diferente al comportamiento base. |
| Método    | `cambiar_limite(nuevo)`   | Actualiza el margen permitido.                       |
| Método    | `info()`                  | Muestra los datos de la cuenta.                      |

### Clase `CajaAhorro(Cuenta)`

| Tipo      | Nombre                | Descripción                                       |
|-----------|-----------------------|---------------------------------------------------|
| Atributo  | `tasa_interes`        | Porcentaje que se aplica periódicamente.          |
| Método    | `aplicar_interes()`   | Ajusta el saldo según la tasa.                    |
| Método    | `cambiar_tasa(nueva)` | Actualiza el porcentaje.                          |
| Método    | `info()`              | Muestra los datos de la cuenta.                   |

### Clase `Transferencia`

| Tipo      | Nombre        | Descripción                                              |
|-----------|---------------|----------------------------------------------------------|
| Atributo  | `origen`      | Cuenta desde donde sale el dinero.                       |
| Atributo  | `destino`     | Cuenta hacia donde va el dinero.                         |
| Atributo  | `monto`       | Cuánto se mueve.                                         |
| Método    | `ejecutar()`  | Concreta el movimiento entre las cuentas.                |
| Método    | `revertir()`  | Deshace el movimiento.                                   |
| Método    | `resumen()`   | Muestra una descripción del movimiento.                  |

### Clase `Banco`

| Tipo      | Nombre                                                | Descripción                                     |
|-----------|-------------------------------------------------------|-------------------------------------------------|
| Atributo  | `nombre`                                              | Denominación de la entidad.                     |
| Atributo  | `clientes`                                            | Personas registradas.                           |
| Atributo  | `cuentas`                                             | Cuentas administradas.                          |
| Atributo  | `transferencias`                                      | Movimientos históricos.                         |
| Método    | `registrar_cliente(c)`                                | Suma una persona.                               |
| Método    | `abrir_cuenta(cuenta)`                                | Suma una cuenta.                                |
| Método    | `realizar_transferencia(origen, destino, monto)`      | Genera y ejecuta un movimiento.                 |
| Método    | `saldo_total_del_banco()`                             | Suma los valores de todas las cuentas.          |

---

## Ejercicio 9 — Torneo de fútbol

Modelar una liga con equipos, jugadores y partidos.

### Clase `Persona`

| Tipo      | Nombre               | Descripción                              |
|-----------|----------------------|------------------------------------------|
| Atributo  | `nombre`             | Cómo se llama.                           |
| Atributo  | `dni`                | Documento identificatorio.               |
| Atributo  | `edad`               | Años que tiene.                          |
| Método    | `mostrar_datos()`    | Muestra su información.                  |
| Método    | `cumplir_anios()`    | Incrementa la edad en 1.                 |
| Método    | `__str__()`          | Representación como texto.               |

### Clase `Jugador(Persona)`

| Tipo      | Nombre                | Descripción                                    |
|-----------|-----------------------|------------------------------------------------|
| Atributo  | `posicion`            | Rol en el campo.                               |
| Atributo  | `goles`               | Cantidad convertida.                           |
| Método    | `hacer_gol()`         | Incrementa su marca personal.                  |
| Método    | `mostrar_stats()`     | Muestra su rendimiento.                        |
| Método    | `mostrar_datos()`     | Extiende la información básica.                |

### Clase `DirectorTecnico(Persona)`

| Tipo      | Nombre                    | Descripción                                    |
|-----------|---------------------------|------------------------------------------------|
| Atributo  | `anios_experiencia`       | Cuánto tiempo lleva en el rubro.               |
| Método    | `dar_charla_tecnica()`    | Simula la acción de instruir al equipo.        |
| Método    | `sumar_experiencia()`     | Incrementa el tiempo en el rubro.              |
| Método    | `mostrar_datos()`         | Extiende la información básica.                |

### Clase `Equipo`

| Tipo      | Nombre                    | Descripción                                        |
|-----------|---------------------------|----------------------------------------------------|
| Atributo  | `nombre`                  | Denominación del equipo.                           |
| Atributo  | `dt`                      | Quién lo dirige (referencia externa).              |
| Atributo  | `jugadores`               | Plantel (referencias externas).                    |
| Atributo  | `puntos`                  | Puntaje acumulado en el torneo.                    |
| Método    | `agregar_jugador(j)`      | Suma alguien al plantel.                           |
| Método    | `sumar_puntos(cantidad)`  | Incrementa el puntaje.                             |
| Método    | `total_goles()`           | Suma lo convertido por todo el plantel.            |
| Método    | `mostrar_plantel()`       | Muestra a todos los del equipo.                    |

### Clase `Partido`

| Tipo      | Nombre                       | Descripción                                       |
|-----------|------------------------------|---------------------------------------------------|
| Atributo  | `local`                      | Equipo que juega en casa.                         |
| Atributo  | `visitante`                  | Equipo que va de visita.                          |
| Atributo  | `goles_local`                | Tantos del local.                                 |
| Atributo  | `goles_visitante`            | Tantos del visitante.                             |
| Método    | `jugar(goles_l, goles_v)`    | Registra el resultado y actualiza a los equipos.  |
| Método    | `resultado()`                | Devuelve el resultado formateado.                 |
| Método    | `ganador()`                  | Devuelve al equipo ganador (o empate).            |

### Clase `Torneo`

| Tipo      | Nombre                       | Descripción                                       |
|-----------|------------------------------|---------------------------------------------------|
| Atributo  | `nombre`                     | Denominación del torneo.                          |
| Atributo  | `equipos`                    | Participantes inscritos.                          |
| Atributo  | `partidos`                   | Encuentros programados/jugados.                   |
| Método    | `inscribir_equipo(e)`        | Suma un participante.                             |
| Método    | `programar_partido(p)`       | Suma un encuentro.                                |
| Método    | `tabla_posiciones()`         | Muestra a los participantes ordenados.            |
| Método    | `goleador_del_torneo()`      | Devuelve al jugador con mayor marca personal.     |

---

## Ejercicio 10 — Editorial

Sistema de una editorial que publica libros.

### Clase `Persona`

| Tipo      | Nombre                | Descripción                              |
|-----------|-----------------------|------------------------------------------|
| Atributo  | `nombre`              | Cómo se llama.                           |
| Atributo  | `dni`                 | Documento identificatorio.               |
| Atributo  | `email`               | Contacto electrónico.                    |
| Método    | `mostrar_datos()`     | Muestra su información.                  |
| Método    | `cambiar_email(nuevo)`| Actualiza el contacto.                   |
| Método    | `__str__()`           | Representación como texto.               |

### Clase `Autor(Persona)`

| Tipo      | Nombre                | Descripción                                    |
|-----------|-----------------------|------------------------------------------------|
| Atributo  | `nacionalidad`        | De dónde proviene.                             |
| Atributo  | `generos`             | Estilos que suele trabajar.                    |
| Método    | `agregar_genero(g)`   | Suma un estilo a su repertorio.                |
| Método    | `mostrar_generos()`   | Muestra su repertorio.                         |
| Método    | `mostrar_datos()`     | Extiende la información básica.                |

### Clase `Editor(Persona)`

| Tipo      | Nombre                | Descripción                                    |
|-----------|-----------------------|------------------------------------------------|
| Atributo  | `anios_experiencia`   | Cuánto tiempo lleva en el rubro.               |
| Método    | `revisar(libro)`      | Actúa sobre un libro cambiando su etapa.       |
| Método    | `aprobar(libro)`      | Da el visto bueno para el siguiente paso.      |
| Método    | `mostrar_datos()`     | Extiende la información básica.                |

### Clase `Libro`

| Tipo      | Nombre                | Descripción                                             |
|-----------|-----------------------|---------------------------------------------------------|
| Atributo  | `titulo`              | Cómo se llama.                                          |
| Atributo  | `genero`              | Estilo que trabaja.                                     |
| Atributo  | `paginas`             | Cuántas hojas tiene.                                    |
| Atributo  | `autor`               | Quién lo escribió (referencia externa).                 |
| Atributo  | `editor`              | Quién lo revisa (referencia externa, opcional).         |
| Atributo  | `estado`              | Etapa del libro (borrador/revisado/publicado).          |
| Método    | `marcar_revisado()`   | Cambia la etapa a revisado.                             |
| Método    | `publicar()`          | Cambia la etapa a la final.                             |
| Método    | `info()`              | Muestra los datos generales.                            |

### Clase `Publicacion`

| Tipo      | Nombre                       | Descripción                                       |
|-----------|------------------------------|---------------------------------------------------|
| Atributo  | `libro`                      | Referencia al material publicado.                 |
| Atributo  | `fecha`                      | Cuándo se publica.                                |
| Atributo  | `tirada`                     | Cantidad de copias.                               |
| Método    | `imprimir_copias(cantidad)`  | Suma copias a la tirada.                          |
| Método    | `resumen()`                  | Muestra una descripción global.                   |
| Método    | `cambiar_tirada(nueva)`      | Actualiza la cantidad de copias.                  |

### Clase `Editorial`

| Tipo      | Nombre                              | Descripción                                     |
|-----------|-------------------------------------|-------------------------------------------------|
| Atributo  | `nombre`                            | Denominación de la empresa.                     |
| Atributo  | `autores`                           | Autores con los que trabaja.                    |
| Atributo  | `editores`                          | Editores en plantilla.                          |
| Atributo  | `libros`                            | Libros registrados.                             |
| Atributo  | `publicaciones`                     | Publicaciones concretadas.                      |
| Método    | `contratar_autor(a)`                | Suma un autor.                                  |
| Método    | `contratar_editor(e)`               | Suma un editor.                                 |
| Método    | `registrar_libro(l)`                | Deja constancia de un libro.                    |
| Método    | `publicar_libro(libro, tirada)`     | Genera una nueva publicación.                   |
| Método    | `libros_publicados()`               | Filtra los libros según su etapa.               |
| Método    | `libros_por_genero(genero)`         | Filtra los libros por estilo.                   |
