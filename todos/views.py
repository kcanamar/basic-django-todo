from django.shortcuts import render
# import the Todo model from the .models module
from .models import Todo

def index(request):
    # create a variable that conatins all todos from the db
    todos = Todo.objects.all()
    
    # first argument is the request object
    # second argument is the view file defined in the template directory
    # thrid argument is the data to be passed to the template view
    return render(request, 'index.html', {'todos': todos})