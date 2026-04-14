from models.userModel import UsuarioModel
from models.schemasModel import userSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, email, password):
        try:
            nuevo_usuario = userSchema(nombre=nombre, email=email, password=password)
            success = self.model.registrar(nuevo_usuario)
            return success ,"Usuario registrado exitosamente." 
        except ValidationError as e:
            return False, e.errors()[0]['msg']