class UsuarioAdmin(Persona):
    def __init__(self, alta=None, idDni=None, nombre=None, apellido=None, nacimiento=None, mail=None, lugar=None, id_usuario_admin=None):
        super().__init__(idDni, nombre, apellido, nacimiento, mail, lugar)
        self.id_usuario_admin = id_usuario_admin  # Por defecto entra en None
        self.alta = alta
    def añadirListaUsuarioAdmin(self, lista):
        lista.append(self)
    def mostrarPerfilAdmin(self):
        return f"Datos Admin:\nID: {self.id_usuario_admin}.\nDNI: {self.idDni}.\nNombre y apellido: {self.nombre} {self.apellido}.\n Mail: {self.mail}"

admin1 = UsuarioAdmin( alta="2026-06-25",idDni=39123456,nombre="Martín",apellido="Silva",nacimiento="1996-08-14",mail="martin.silva@mail.com",lugar="Córdoba"
)