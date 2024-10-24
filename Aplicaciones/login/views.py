from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from .forms import PasswordResetRequestForm
from .models import MyUser
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.forms import AuthenticationForm

def signin(request):
    if request.method == 'GET':
        return render(request, 'loginviews.html')
    else:
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        
        if user is None:
            print("Autenticación fallida.")
            return render(request, 'loginviews.html', {
            'error': 'Correo electrónico o contraseña incorrectos.'
        })
        else:
            login(request, user)
            print("Sesión iniciada para el usuario:", user.correo_electronico)
            
            # Verificar si el usuario es superuser
            if user.is_superuser:
                print("Usuario superuser, redirigiendo a la página de inicio.")
                return redirect(reverse('inicio:listarActividades'))

            grupos_usuario = list(user.groups.values_list('name', flat=True))
            print("Grupos del usuario:", grupos_usuario)

            # Redirigir según el rol del usuario
            if 'Vendedor' in grupos_usuario:
                print("Usuario con rol Vendedor, redirigiendo a presupuestos:home.")
                return redirect(reverse('presupuestos:home'))
            elif 'Facturador' in grupos_usuario:
                print("Usuario con rol Facturador, redirigiendo a facturas:listarFacturas.")
                return redirect(reverse('facturas:listarFacturas'))
            elif 'Asesor de Ventas' in grupos_usuario:
                print("Usuario con rol Asesor de Ventas, redirigiendo a ventas:home.")
                return redirect(reverse('ventas:home'))
            else:
                # Si el rol no es válido, redirigir a la página de inicio
                print("Rol desconocido, redirigiendo a la página de inicio.")
                return render(request, 'loginviews.html', {
                        'error': 'Correo electrónico o contraseña incorrectos.'
                    })
        
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('signin'))

def passwordResetRequestView(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = MyUser.objects.get(correo_electronico=email)
            except MyUser.DoesNotExist:
                user = None

            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                current_site = get_current_site(request)
                mail_subject = 'Restablecer contraseña'
                reset_link = f"http://{current_site.domain}{reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})}"
                message = (
                    f"Hola estimado,\n\n"
                    "Recibimos una solicitud para restablecer la contraseña de su cuenta.\n\n"
                    f"Haga clic en el enlace a continuación para restablecer su contraseña:\n\n"
                    f"{reset_link}\n\n"
                    "Si no solicitó este cambio, ignore este correo electrónico."
                )
                send_mail(mail_subject, message, 'consortiumsolutionsarg@gmail.com', [email])
                return redirect('password_reset_done')
            else:
                error_message = "No hay ningún registro con ese correo electrónico. py"
            return render(request, 'formRestablecerContrasenia.html', {'error_message': error_message})
    return render(request, 'formRestablecerContrasenia.html')