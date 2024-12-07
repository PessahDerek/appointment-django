from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.method == 'POST':
        return redirect("")
    return render(request, 'dashboard.html')
