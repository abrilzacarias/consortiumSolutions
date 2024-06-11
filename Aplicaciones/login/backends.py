from django.contrib.auth.backends import BaseBackend
from .models import MyUser

class MiUsuarioBackend(BaseBackend):
    def authenticate(self, request, correo_electronico=None, password=None):
        try:
            user = MyUser.objects.get(correo_electronico=correo_electronico)

            print(user.__dict__)

            print(f"Usuario encontrado en la base de datos: {user}")
            if user.check_password(raw_password=password):
                print("Contraseña válida.")
                return user
            else:
                print("Contraseña incorrecta.")
                print("Resultado de check_password:", user.check_password(password))
        except MyUser.DoesNotExist:
            print("Usuario no encontrado en la base de datos.")
            return None
