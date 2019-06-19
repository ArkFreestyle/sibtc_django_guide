from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
def home(request):
    """Any view function takes a request, and returns a response"""
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
    