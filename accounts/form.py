from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class Create(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'age']

class Change(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'age']
