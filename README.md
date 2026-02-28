## Sistema Avanzado de Gestión de Inventario – Tienda de Cosméticos

## Descripción

Este proyecto consiste en el desarrollo de un sistema avanzado de gestión de inventario para una tienda de cosméticos, implementado en Python utilizando Programación Orientada a Objetos (POO).

El sistema permite administrar productos mediante un menú interactivo en consola, facilitando operaciones como agregar, eliminar, actualizar, buscar y visualizar productos. Además, incorpora almacenamiento persistente en archivos para conservar la información del inventario.


## Aplicación de Programación Orientada a Objetos (POO)

El sistema está estructurado en modelos y servicios:

### Modelos

🔹 Clase Producto

Representa cada producto del inventario e incluye:

Atributos privados (encapsulamiento):
- ID
- Nombre
- Cantidad
- Precio

Métodos getters y setters para acceder y modificar los atributos.

Método especial __str__ para mostrar la información del producto de forma legible.

Esto permite proteger los datos y mantener una estructura organizada.

### Servicios
  
🔹 Clase Inventario

Encapsula la lógica de gestión del sistema:
- Añadir nuevos productos.
- Eliminar productos por ID.
- Actualizar cantidad y precio.
- Buscar productos por nombre.
- Mostrar todos los productos.
- Guardar y cargar datos desde archivo.

Separa la lógica del inventario del sistema principal, aplicando el principio de responsabilidad única.


## Uso de Colecciones

El sistema utiliza diferentes colecciones de Python:

### 🔸 Diccionario
self.productos = {}

Se utiliza un diccionario donde:

La clave es el ID del producto.

El valor es un objeto de la clase Producto.

Esto permite búsquedas rápidas y eficientes por ID (acceso directo).

### 🔸 Lista

Se emplea una lista para almacenar los resultados de búsqueda cuando se buscan productos por nombre.

### 🔸 Tupla

Se define una tupla con categorías válidas de productos:

self.categorias_validas = ("Maquillaje", "Skincare", "Accesorios")

La tupla se utiliza porque representa datos fijos que no deben modificarse durante la ejecución del programa.

## Persistencia de Datos

El inventario se almacena en un archivo de texto (inventario.txt).

Se implementa:

- Escritura de datos mediante open() en modo "w".

- Lectura de datos mediante open() en modo "r".

- Uso del administrador de contexto with para garantizar el cierre automático del archivo.

### 🔹 Serialización

Cada producto se guarda en el archivo con el formato:

id|nombre|cantidad|precio

### 🔹 Deserialización

Al iniciar el programa, el archivo se lee línea por línea y cada registro se convierte nuevamente en un objeto Producto.

Esto permite mantener los datos incluso después de cerrar el programa.


## Interfaz de Usuario

El sistema cuenta con un menú interactivo en consola que permite al usuario realizar las siguientes operaciones:

- Añadir producto

- Eliminar producto

- Actualizar producto

- Buscar por nombre

- Mostrar todos

- Salir
  

## Cómo ejecutar el programa

Desde la carpeta principal del proyecto:

python main.py
