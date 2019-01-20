from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from gameplay.models import Game

@login_required
def home(request):
    games_first_player = Game.object.filter(
        first_player=request.user,
        status='F'
    )
    games_second_player = Game.object.filter(
        second_player=request.user,
        status='S'
    )
    all_my_games = list(games_first_player) + list(games_second_player)

    return render(request, "player/home.html",
                  {'games': all_my_games,
                   'num_games': Game.object.count(),
                   'n_games': len(all_my_games)})

