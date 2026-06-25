import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def crearTablasAdmin():
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario_admin TEXT PRIMARY KEY,
            dni INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            apellido TEXT,
            nacimiento TEXT,
            mail TEXT,
            lugar TEXT,
            alta TEXT
        )
    """)
    conexion.commit()
    conexion.close()

def crearTablaInsumo():
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS insumos (
            id_insumo TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL,
            stock_minimo INTEGER,
            stock INTEGER
        )
    """)
    conexion.commit()
    conexion.close()

def crearTablaProducto():
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id_producto TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL,
            id_insumo TEXT,
            FOREIGN KEY (id_insumo) REFERENCES insumos (id_insumo) ON DELETE SET NULL
        )
    """)
    conexion.commit()
    conexion.close()

def insertar_usuario(usuario): 
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", 
                   (usuario.idDni, usuario.nombre, usuario.apellido, 
                    usuario.nacimiento, usuario.mail, usuario.lugar, usuario.alta))
    conexion.commit()
    conexion.close()

def mostrar_todos_los_usuario():
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuariosBd = cursor.fetchall()
    if usuariosBd:
        print("\n--- LISTADO DE USUARIOS ADMINISTRADORES ---")
        for usuario in usuariosBd:
            print(f"ID: {usuario[0]}, DNI: {usuario[1]}, Nombre: {usuario[2]}, Detalle: {usuario[3]}, Mail: {usuario[5]}")
    else:
        print("\nNo se encontraron registros de usuarios en la base de datos.")
    conexion.commit()
    conexion.close()

def mostrar_usuario(id_usuario):
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id_usuario_admin = ?", (id_usuario,))
    fila = cursor.fetchone()
    if fila:
        print(f"\nID: {fila[0]}, DNI: {fila[1]}, Nombre: {fila[2]}, Detalle: {fila[3]}, Mail: {fila[5]}")
    else:
        print("\nNo se encontró el usuario solicitado en la base de datos.")
    conexion.commit()
    conexion.close()

def insertar_insumo(insumo):
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO insumos VALUES (NULL, ?, ?, ?, ?)", 
                   (insumo.nombre, insumo.precio, insumo.stock_minimo, insumo.stock))
    insumo.id_insumo = cursor.lastrowid
    conexion.commit()
    conexion.close()

def mostrar_todos_los_insumos():
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM insumos")
    insumosBd = cursor.fetchall()
    if insumosBd:
        print("\n--- LISTADO DE INSUMOS ---")
        for insumo in insumosBd:
            print(f"ID: {insumo[0]}, Nombre: {insumo[1]}, Precio: ${insumo[2]:.2f}, Stock: {insumo[4]}")
    else:
        print("\nNo se encontraron registros de insumos en la base de datos.")
    conexion.commit()
    conexion.close()

def mostrar_insumo(id_insumo):
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM insumos WHERE id_insumo = ?", (id_insumo,))
    insumo = cursor.fetchone()
    if insumo:
        print(f"\nID: {insumo[0]}, Nombre: {insumo[1]}, Precio: ${insumo[2]:.2f}, Stock: {insumo[4]}")
    else:
        print(f"\nNo se encontró ningún insumo con el ID: '{id_insumo}'")
    conexion.commit()
    conexion.close()

def insertar_producto(producto):
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    id_insumo_asoc = producto.objeto_insumo.id_insumo if producto.objeto_insumo else None
    cursor.execute("INSERT INTO productos VALUES (NULL, ?, ?, ?)", 
                   (producto.nombre, producto.precio, id_insumo_asoc))
    producto.id_producto = cursor.lastrowid
    conexion.commit()
    conexion.close()

def mostrar_todos_los_productos():
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productosBd = cursor.fetchall() 
    if productosBd:
        print("\n--- LISTADO DE PRODUCTOS ---")
        for producto in productosBd:
            insumo_asoc = producto[3] if producto[3] else "Ninguno"
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}, Insumo ID: {insumo_asoc}")
    else:
        print("\nNo se encontraron registros de productos en la base de datos.")
    conexion.commit() 
    conexion.close()

def mostrar_producto(id_producto):
    conexion = sqlite3.connect("TpFinalDB")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
    producto = cursor.fetchone() 
    if producto:
        insumo_asoc = producto[3] if producto[3] else "Ningun insumo"
        print(f"\nID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}, Insumo Contenido (ID): {insumo_asoc}")
    else:
        print(f"\nNo se encontró ningún producto con el ID: '{id_producto}'")
    conexion.commit()
    conexion.close()