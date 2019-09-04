from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

import snake
import time


def index(request):
    return render(request, 'snakegame/index.html')

def new_game(request):
    snake.reset_game()
    snake.create_new_board()
    board = snake.Snake.board
    return render(request, 'snakegame/game.html', {
        'board' : board
    })

def game(request):
    move = request.POST.get('move_key')
    if move == 'w' or move == 's' or move =='a' or move == 'd':
        snake.Snake.currentMove =  move.upper()
    snake.random_treats()
    ans = snake.next_move()
    if (ans == 'The end'):
        return render(request, 'snakegame/the_end.html',{
            'score' : len(snake.Snake.snakeBody)
        })
    return render(request, 'snakegame/game.html',{
        'board' : snake.Snake.board
    })
