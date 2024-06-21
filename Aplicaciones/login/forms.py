from django import forms

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico", max_length=512)
