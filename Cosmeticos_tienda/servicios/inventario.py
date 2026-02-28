import os
from modelos.producto import Producto

# Clase Inventario que gestiona los productos utilizando un diccionario para almacenamiento
class Inventario:
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        self.ruta_archivo = os.path.join(base_dir, "datos", "inventario.txt")
       
       # Se utiliza un diccioario donde:
       # - La clave es el ID del producto
       # - El valor es un objeto producto.
        self.productos = {}  

# Tupla para almacenar categorías fijas ya que mo deben ser modificadas por el usuario.
        self.categorias_validas = ("maquillaje", "skincare", "accesorios")
       
        self.cargar_inventario()

# Crear archivo si no existe
    def verificar_archivo(self):
        carpeta = os.path.dirname(self.ruta_archivo)

        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        if not os.path.exists(self.ruta_archivo):
    
    # Escritura de archivos en modo "w" para crear el archivo vacío si no existe.
            with open(self.ruta_archivo, "w", encoding="utf-8"):
                pass

# Guardar inventario en el archivo
    def guardar_inventario(self):
        self.verificar_archivo()

        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            for producto in self.productos.values():
                linea = f"{producto.get_id()}|{producto.get_nombre()}|{producto.get_cantidad()}|{producto.get_precio()}"
                archivo.write(linea + "\n")

# Cargar inventario desde el archivo
    def cargar_inventario(self):
        self.verificar_archivo()
        self.productos.clear()

    # Lectura de archivos en modo "r" para cargar los productos existentes.
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                partes = linea.split("|")
                if len(partes) != 4:
                    continue

                try:
                    id_p = int(partes[0])
                    nombre = partes[1]
                    cantidad = int(partes[2])
                    precio = float(partes[3])

                    producto = Producto(id_p, nombre, cantidad, precio)
                    self.productos[id_p] = producto

                except ValueError:
                    continue

# Añadir nuevo producto al inventario
    def agregar_producto(self):
        try:
            id_p = int(input("ID del producto: "))

            if id_p in self.productos:
                print("⚠️ Ya existe un producto con ese ID.")
                return

            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            nuevo = Producto(id_p, nombre, cantidad, precio)
            self.productos[id_p] = nuevo
            
            self.guardar_inventario()
            print("✅ Producto agregado correctamente.")

        except ValueError:
            print("⚠️ Error en los datos ingresados.")

# Eliminar producto del inventario
    def eliminar_producto(self):
        try:
            id_p = int(input("ID del producto a eliminar: "))

            if id_p in self.productos:
                del self.productos[id_p]
                self.guardar_inventario()
                print("🗑️ Producto eliminado.")
            else:
                print("❌ Producto no encontrado.")

        except ValueError:
            print("⚠️ ID inválido.")

# Actualizar cantidad y precio de un producto existente
    def actualizar_producto(self):
        try:
            id_p = int(input("ID del producto a actualizar: "))

            if id_p not in self.productos:
                print("❌ Producto no encontrado.")
                return

            producto = self.productos[id_p]

            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))

            producto.set_cantidad(nueva_cantidad)
            producto.set_precio(nuevo_precio)

            self.guardar_inventario()
            print("✅ Producto actualizado.")

        except ValueError:
            print("⚠️ Datos inválidos.")

# Buscar productos por nombre (búsqueda parcial)
    def buscar_por_nombre(self):
        nombre_buscar = input("Nombre a buscar: ").lower()
        
# Se utiliza una lista para almacenar los resultados de búsqueda por nombre.
        encontrados = []

        for producto in self.productos.values():
            if nombre_buscar in producto.get_nombre().lower():
                encontrados.append(producto)

        if encontrados:
            print("\n🔎 Resultados:")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos.")

 # Mostrar todos los productos en el inventario
    def mostrar_todos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        print("\n📋 LISTA DE PRODUCTOS")
        for producto in self.productos.values():
            print(producto)
   