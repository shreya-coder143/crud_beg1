from django.shortcuts import render
from crudapp.forms import UserForm
from django.http import HttpResponse

# Create your views here.
def insert(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("<h1>data sent to database...</h1>")
            except:
                pass
    form=UserForm()
    return render(request,'index.html',{'form':form})