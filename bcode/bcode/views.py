from django.shortcuts import render

def welcome(request):
    return render(request, 'bcode/welcome.html')