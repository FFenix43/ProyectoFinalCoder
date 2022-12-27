from django import forms


class SignupForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    gmail=forms.EmailField()
    contra=forms.CharField(label="contraseña", widget=forms.PasswordInput, strip=False)
    confirmar=forms.CharField(label="confirmar", widget=forms.PasswordInput, strip=False)


