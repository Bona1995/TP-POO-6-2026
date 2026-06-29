class Persona:
    def __init__(self, id_dni:int=None, nombre=None, apellido=None, nacimiento=None, mail=None, lugar=None):
        self.idDni = id_dni          
        self.nombre = nombre         
        self.apellido = apellido      
        self.nacimiento = nacimiento  
        self.mail = mail              
        self.lugar = lugar  
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        nuevo_nombre = nuevo_nombre.strip()
        if not nuevo_nombre.isalpha() or len(nuevo_nombre)>15:
            raise ValueError("Error de tipeo, solo letras y con longitud menor a 15 caracteres")
        else:
            self._nombre = nuevo_nombre
    @property
    def mail(self):
        return self._mail
    @mail.setter
    def mail(self, nuevo_mail):
        nuevo_mail = nuevo_mail.strip()    
        if nuevo_mail.strip:
            posicion_arroba = nuevo_mail.find("@")        
            if posicion_arroba:
                posicion_usuario = nuevo_mail[:posicion_arroba]
                posicion_dominio = nuevo_mail[posicion_arroba+1:]                 
                if " " not in posicion_usuario: 
                    if " " not in posicion_dominio and posicion_dominio.endswith(".com"):
                        self._mail = nuevo_mail
                    else:
                        raise ValueError("Error, campo mail con dominio incorrecto, vuelva a ingresarlo")       
                else:
                    raise ValueError("Error, campo mail con espacios, vuelva a ingresarlo")      
            else:
                raise ValueError("Error, campo mail invalido, vuelva a ingresarlo")        
        else:
            raise ValueError("Error, campo mail vacio, vuelva a ingresarlo") 
    def MostrarDatosPersona(self):
        return f"Datos personales:\nDNI: {self.IdDni}.\nNombre y apellido: {self.nombre} {self.apellido}.\nMail: {self.mail}"