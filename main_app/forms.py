from django import forms
# this is how you get custom usermodel
from django.contrib.auth import get_user_model
User = get_user_model()


# class UserCreationForm(forms.Form):
#     username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'id': 'username', 'style': 'width: 300px;', 'class': 'form-control'}))
#     password = forms.CharField(widget = forms.PasswordInput(attrs={ 'id': 'password', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
#     confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'id': 'confirm_password', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={'id': 'username', 'style': 'width: 300px;', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={ 'id': 'password', 'style': 'width: 300px;', 'class': 'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'id': 'confirm_password', 'style': 'width: 300px;', 'class': 'form-control'})
        }
