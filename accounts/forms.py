from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Mots de passe"}))

