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

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Recibido - Usuario: {username}, Contraseña: {password}")

        user = authenticate(request, correo_electronico=username, password=password)
        print(f"Resultado de autenticación: {user}")

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('inicio:listarActividades'))
        else:
            error_message = "Correo electrónico o contraseña incorrectos."
            return render(request, 'loginviews.html', {'error_message': error_message})
    return render(request, 'loginviews.html')

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def indexView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))  
    return render(request, 'inicio/index.html')  

def resetPasswordView(request):
    return render(request, 'formRestablecerContrasenia.html')

def passwordResetRequestView(request):
    error_message = None 
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
                mail_subject = 'Restablecer su contraseña'
                reset_link = f"http://{current_site.domain}{reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})}"
                message = (
                    f"Hola {user.nombre_usuario},\n\n"
                    "Recibimos una solicitud para restablecer la contraseña de su cuenta.\n\n"
                    f"Haga clic en el enlace a continuación para restablecer su contraseña:\n\n"
                    f"{reset_link}\n\n"
                    "Si no solicitó este cambio, ignore este correo electrónico."
                )
                send_mail(mail_subject, message, 'consortiumsolutionsarg@gmail.com', [email])
                return redirect('password_reset_done')
            else:
                error_message = "No hay ningún registro con ese correo electrónico."
    else:
        form = PasswordResetRequestForm()
    return render(request, 'formRestablecerContrasenia.html', {'form': form, 'error_message': error_message})

