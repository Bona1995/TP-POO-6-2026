import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Datos.BaseDeDatos2TP import *

def opcion_registrar_usuario():
    print("\n--- NUEVO ADMINISTRADOR ---")
    alta = input("Fecha Alta: ")
    dni = int(input("DNI (números): "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    nacimiento = input("Fecha de Nacimiento (AAAA-MM-DD): ")
    mail = input("Mail: ")
    lugar = input("Lugar: ")
    
    nuevo_admin = UsuarioAdmin(alta=alta,idDni=dni, nombre=nombre,apellido=apellido,nacimiento=nacimiento,mail=mail,lugar=lugar)
    insertar_usuario(nuevo_admin)
    return f"¡Administrador guardado exitosamente en el sistema!: {nuevo_admin}"
    
    admin5= UsuarioAdmin(dniAdmin, nombreAdmin, apellidoAdmin,  nacimientoAdmin, mailAdmin,  lugarAdmin, idAdmin)
    admin5= mostrarPerfilAdmin()

def opcion_registrar_insumo():
    print("\n--- NUEVO INSUMO ---")
    nombre = input("Nombre Insumo: ")
    precio = float(input("Precio: $"))
    stock_min = int(input("Stock Mínimo: "))
    stock = int(input("Stock Actual: "))

    nuevo_insumo = Insumo(nombre=nombre, precio=precio, stock_minimo=stock_min, stock=stock)   
    insertar_insumo(nuevo_insumo)
    return f"¡Insumo guardado exitosamente en en el sistema!: {nuevo_insumo}"

def opcion_registrar_producto():
    print("\n--- NUEVO PRODUCTO ---")
    nombre = input("Nombre Producto: ")
    precio = float(input("Precio: $"))
    id_insumo_asoc = input("Ingrese el ID del Insumo que contiene (Deje vacío si no contiene ninguno): ").strip()
 
    insumo_objeto = None
    if id_insumo_asoc:
        conexion = sqlite3.connect("TpFinalDB")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM insumos WHERE id_insumo = ?", (id_insumo_asoc,))
        fila = cursor.fetchone()
        conexion.close()
        if fila:
            insumo_objeto = Insumo(id_insumo=fila[0], nombre=fila[1], precio=fila[2], stock_minimo=fila[3], stock=fila[4])
        else:
            print("El ID de insumo no existe. Se creará el producto sin insumo.")

    nuevo_producto = Producto(nombre=nombre, precio=precio, insumo=insumo_objeto)
    insertar_producto(nuevo_producto) 
    return "¡Producto guardado exitosamente en la Base de Datos!"


def login(usuario, contraseña):
    while True:
        passOk=False #Centinela de cambio de estado. Permite romper el bucle ya que en el for no se puede
        for n in range (3, 0, -1): # Inicio de sesion con bucle for, se itera 3 veces y se validan los datos. 
            _usuarioIngreso= input("Nombre de usuario: ")
            _contraseIngreso= input("Contraseña: ")
            if n!=1:
                if _usuarioIngreso == usuario:
                    if _contraseIngreso == contraseña:
                        passOk=True
                        print("Bienvenido!")
                        break          
                    else:
                        print(f"Contraseña invalida, le quedan {n-1} intentos ")    
                else:
                    print(f"Usuario inexistente, le quedan {n-1} intentos")
            else:             
                for i in range (5, 0, -1): # Debera esperar 5 segundos para volver a ingresar sus credenciales, se intera con time.sleep
                    time.sleep(1)
                    print(f"Se bloqueo su acceso, vuelva a intentar en: {i}")  
        if passOk: # Hasta no tener un inicio de sesion exitosos no supera el bucle de ingreso.
            break 
    return passOk          

def cargar_datos_prueba():
    try:
        # 1. Creamos el Administrador
        admin_prueba = UsuarioAdmin(alta="2026-06-25", idDni=39123456, nombre="Martín", apellido="Silva", nacimiento="1996-08-14", mail="martin.silva@mail.com", lugar="Córdoba")
        insertar_usuario(admin_prueba)
        
        # 2. Creamos los Insumos sueltos en memoria
        insumo1 = Insumo(nombre="Azucar", precio=50.0, stock_minimo=20, stock=50)
        insumo2 = Insumo(nombre="Sal", precio=30.0, stock_minimo=15, stock=30)
        
        # 3. Los insertamos (las funciones ahora actualizan el ID gracias al lastrowid)
        insertar_insumo(insumo1)
        insertar_insumo(insumo2)
        
        # 4. Ahora que insumo1 e insumo2 tienen sus IDs reales de SQLite, creamos los productos
        producto1 = Producto(nombre="Alfajor Santafesino", precio=150.0, insumo=insumo1)
        producto2 = Producto(nombre="Galletitas de Agua", precio=90.0, insumo=insumo2)
        
        # 5. Los guardamos en la BD
        insertar_producto(producto1)
        insertar_producto(producto2)
        
        print("\n[Sistema]: Entorno de prueba inicializado correctamente.")
        
    except Exception as e:
        pass

def menu_principal():
    crearTablasAdmin()
    crearTablaInsumo()
    crearTablaProducto()
    
    cargar_datos_prueba()
    
    while True:
        print("   MENÚ DE GESTIÓN ACADÉMICA / COMERCIAL   ")
        print("1. Registrar Usuario Administrador")
        print("2. Mostrar Todos los Usuarios")
        print("3. Buscar Usuario por ID")
        print("4. Registrar Insumo")
        print("5. Mostrar Todos los Insumos")
        print("6. Buscar Insumo por ID")
        print("7. Registrar Producto (Contención Débil)")
        print("8. Mostrar Todos los Productos")
        print("9. Buscar Producto por ID")
        print("0. Salir")
        opcionMatch = input("Seleccionar una opción del 0 al 9: ").strip()
        if not opcionMatch:
            print("\n[Error]: Ingreso de opción inválido, vuelva a intentarlo.")
            continue  
        if opcionMatch not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("\n[Error]: Ingreso de opción fuera de rango, vuelva a intentarlo.")
            continue
        match opcionMatch:
            case "1":
                print("1. Registrar Usuario Administrador \n")
                resultadoUsuario= opcion_registrar_usuario()
                print(f"{resultadoUsuario}")
            case "2":
                print("2. Mostrar Todos los Usuarios \n")
                resultadoMostrarUsuarios = opcion_mostrar_usuarios()
                print(f"{resultadoMostrarUsuarios}")
            case "3":
                print("3. Buscar Usuario por ID \n")
                resultadoBuscarUsuario = opcion_buscar_usuario()
                print(f"{resultadoBuscarUsuario}")
            case "4":
                print("4. Registrar Insumo \n")
                resultadoInsumo = opcion_registrar_insumo()
                print(f"{resultadoInsumo}")
            case "5":
                print("5. Mostrar Todos los Insumos \n")
                resultadoMostrarInsumos = opcion_mostrar_insumos()
                print(f"{resultadoMostrarInsumos}")
            case "6":
                print("6. Buscar Insumo por ID \n")
                resultadoBuscarInsumo = opcion_buscar_insumo()
                print(f"{resultadoBuscarInsumo}")
            case "7":
                print("7. Registrar Producto \n")
                resultadoProducto = opcion_registrar_producto()
                print(f"{resultadoProducto}")
            case "8":
                print("8. Mostrar Todos los Productos \n")
                resultadoMostrarProductos = opcion_mostrar_productos()
                print(f"{resultadoMostrarProductos}")
            case "9":
                print("9. Buscar Producto por ID \n")
                resultadoBuscarProducto = opcion_buscar_producto()
                print(f"{resultadoBuscarProducto}")
            case "0":
                print("Saliendo del menu, gracias por usar!. \n")
                break