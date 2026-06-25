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



def validarSelectorMenu(minimo=1, maximo=9): 
    while True:
        opciones= input(f"Seleccionar una opción del {minimo} al {maximo}: ")
        if not opciones.isdigit():
            print("Ingreso de opcion invalido, vuelva a intentarlo.")
            continue 
        opcion_int= int(opciones) # Casteamos el ingreso de opcion a entero para validar la opcion
        if (opcion_int < minimo  or opcion_int > maximo): # Validamos solo rangos entre los paramatros 1 a 5
            print("Ingreso de opcion fuera de rango, vuelva a intentarlo.")
            continue
        else:
            break
    return opcion_int

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

def menu_principal():
    crearTablasAdmin()
    crearTablaInsumo()
    crearTablaProducto()
    
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
        opcionMatch = validarSelectorMenu()
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