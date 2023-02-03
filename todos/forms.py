# import models
from .models import Todo
from django.forms import ModelForm

# create the form class
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'details']