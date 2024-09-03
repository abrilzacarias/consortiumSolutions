from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El campo correo electrónico debe estar establecido')
        
        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=correo_electronico, **extra_fields)
        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_electronico, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')

        return self.create_user(correo_electronico, password, **extra_fields)

    def authenticate(self, request, correo_electronico=None, password=None):
        print(f"Recibido - Correo electrónico: {correo_electronico}, Contraseña: {password}")

        try:
            user = MyUser.objects.get(correo_electronico=correo_electronico)
            print(f"Usuario encontrado en la base de datos: {user.correo_electronico}")
            
            if user.check_password(password):
                print("Contraseña correcta.")
                return user
            else:
                print("Contraseña incorrecta.")
                print("Resultado de check_password:", user.check_password(password))
        except MyUser.DoesNotExist:
            print("Usuario no encontrado en la base de datos.")
            return None

class MyUser(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    correo_electronico = models.EmailField(unique=True, max_length=255)
    nombre_usuario = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    # Relaciones con modelos predefinidos
    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',  # Puedes cambiar el nombre de la relación si lo prefieres
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users',  # Puedes cambiar el nombre de la relación si lo prefieres
        blank=True
    )


    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre_usuario']

    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users',
        blank=True
    )
    
    def __str__(self):
        return self.correo_electronico
