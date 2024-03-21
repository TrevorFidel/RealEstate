from django.shortcuts import render
from .form import RegisterForm, RegistrationForm

# Create your views here.
def index(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form = RegistrationForm()
    return render(request, 'index.html', {'form': form})
def about(request):
    return render(request, 'about.html')
def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def logout(request):
    return render(request, 'logout.html')

