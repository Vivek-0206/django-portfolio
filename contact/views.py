from django.shortcuts import render


def home(request):

    return render(request, 'contact/main.html')
