from django.shortcuts import render
# import the Todo model from the .models module
from .models import Todo
# import form model
from .forms import TodoForm
# import http redirect response
from django.http import HttpResponseRedirect

def index(request):
    # create logic for different http methods
    if(request.method == "POST"):
        # # create a new form instance and populate with data from the request
        # form = TodoForm(request.POST)
        # # print the property of the request dict
        # print(request.POST.get('title'))
        # use the Todo model to create new todo from request dict
        Todo.objects.create(
            title=request.POST.get('title'),
            details=request.POST.get('details')
        )
        return HttpResponseRedirect("/index/")
        
    if(request.method == "GET"):     
        # create a variable that conatins all todos from the db
        todos = Todo.objects.all()
    
        # create form
        form = TodoForm()
        # first argument is the request dictonary
        # second argument is the view file defined in the template directory
        # thrid argument is the data to be passed to the template view
        # pass form as second property to data dictonary
        return render(request, 'index.html', {'todos': todos, 'form': form})