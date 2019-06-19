from django.shortcuts import render, get_object_or_404
from .models import Board

# Create your views here.
def home(request):
    """Any view function takes a request, and returns a response"""
    
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
    

def board_topics(request, pk):
    """Function renders the board topics page"""

    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    """View for creating new topics"""

    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})
    