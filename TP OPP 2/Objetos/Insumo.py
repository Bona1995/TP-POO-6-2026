class Insumo:
    def __init__(self, id_insumo=None, nombre=None, precio=None, stock_minimo=5, stock=None):
        self.id_insumo = id_insumo
        self.nombre = nombre
        self.precio = precio
        self.stock_minimo = stock_minimo
        self.stock= stock
    def actualizarStock(self, cantidad:int=None):
        if self.stock > self.stock_minimo:
            centinela_info= f"Stock actual: {self.stock}"
            if self.stock >= cantidad:
                self.stock= self.stock - cantidad
                centinela_info= f"Stock modificado, acutalizado: {self.stock}"
                if self.stock < self.stock_minimo:
                    centinela_info = f"Stock modificado, actualizado: {self.stock}.\nPrecaucion!. Nivel critico de stock, solo quedan {self.stock} unidades.\nReponga urgente el insumo {self.id_insumo}, {self.nombre}."  
            else:
                centinela_info= "No es posible, cantidad de insumos menor a la demanda"
        else:
            centinela_info= f"Precaucion!. Nivel critico de stock, solo quedan {self.stock} unidades.\nReponga urgente el insumo {self.id_insumo}, {self.nombre}." 
        return centinela_info
    def mostrarDatosInsumo(self):
        return f"Datos Insumo:\nID: {self.id_insumo}.\nNombre: {self.nombre}.\nPrecio: {self.precio}.\nStock: {self.stock}\n."

insumo1= Insumo(1, "Azucar", "$50", 20, 50)
insumo2= Insumo(2, "Sal", "$30", 15, 30)