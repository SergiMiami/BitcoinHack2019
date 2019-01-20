from django.shortcuts import render, redirect
import sys

def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, 'bcode/welcome.html')