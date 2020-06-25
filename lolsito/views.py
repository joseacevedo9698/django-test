from django.shortcuts import render

# Create your views here.
def summoner_list(request):
    return render(request, 'lolsito/summoner_list.html', {})