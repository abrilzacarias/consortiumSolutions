from django.urls import path
from django.contrib.auth import views as auth_views
from .views import passwordResetRequestView
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),  # La ruta raíz para login
    path('signin/', views.signin, name='signin'),  # Ruta explícita para login
    path('logout/', views.logoutView, name='logout'),
    path('index/', views.indexView, name='index'),
    path('resetPassword/', views.resetPasswordView, name='resetPassword'),
    path('passwordReset/', passwordResetRequestView, name='passwordReset'),
    path('passwordReset/done/', auth_views.PasswordResetDoneView.as_view(template_name='correoEnviado.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='formNuevaContrasenia.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='contraseniaRestablecida.html'), name='password_reset_complete'),
]


