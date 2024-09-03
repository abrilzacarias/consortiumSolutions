from django.contrib import admin
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('correo_electronico', 'nombre_usuario')

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('correo_electronico', 'nombre_usuario', 'is_active', 'is_staff', 'is_superuser')

class MyUserAdmin(admin.ModelAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('correo_electronico', 'nombre_usuario', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    filter_horizontal = ('groups', 'user_permissions')
    fieldsets = (
        (None, {'fields': ('correo_electronico', 'password')}),
        ('Personal info', {'fields': ('nombre_usuario',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined',), 'classes': ('collapse',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correo_electronico', 'nombre_usuario', 'password1', 'password2'),
        }),
    )
    search_fields = ('correo_electronico',)
    ordering = ('correo_electronico',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If obj exists (editing an existing user), make date_joined read-only
            return self.readonly_fields + ('date_joined',)
        return self.readonly_fields

admin.site.register(MyUser, MyUserAdmin)
