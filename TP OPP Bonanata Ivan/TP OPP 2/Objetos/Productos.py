class Producto:
    def __init__(self, nombre=None, precio=None, insumo: "Insumo" = None, id_producto=None):
        self.id_producto = id_producto  # Por defecto entra en None
        self.nombre = nombre
        self.precio = precio
        self.objeto_insumo = insumo
    def verificarProductoALaVenta(self):
        if self.objeto_insumo.actualizarStock:
            centinela_venta= f"El producto {self.nombre} esta disponible"
    def mostrarDatosProducto(self):
        return f"Datos Producto: Nombre: {self.nombre}.\nPrecio: {self.precio}."
