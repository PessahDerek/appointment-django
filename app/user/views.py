from django.shortcuts import render, redirect
from django.http import HttpResponse

from .custom_forms import CustomUserCreationForm
from .models import Patient


# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponse(status=400)
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        # TODO: handle signup
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Very valid")
            found = Patient.objects.get(email=form.cleaned_data['email'])
            if found:
                return render(request, 'signup.html', {'form': form})
            new_user = form.save(commit=False)
            new_user.save()
            # return login(request)
            return redirect('dashboard-home')
        print("Invalid form")
        return render(request, 'signup.html', {'form': form})
    return render(request, 'signup.html', {'is_login': False, 'form': CustomUserCreationForm()})


def login(request):
    if request.method == 'POST':
        # todo: handle login
        """"""""
    return render(request, 'login.html')
