from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from .forms import NewTopicForm


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
    user = User.objects.first()

    if request.method == 'POST':

        form = NewTopicForm(request.POST)
        
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )

            return redirect('board_topics', pk=board.pk)
        
    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})
    