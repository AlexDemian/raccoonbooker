from django.forms import ModelForm

from profiles.models import User

class LoginForm(ModelForm):
    
    class Meta:
        model = User
        fields = ('email', 'password')
    