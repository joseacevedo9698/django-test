from django.shortcuts import render
from django.utils import timezone
from .models import Summoner
# Create your views here.
def summoner_list(request):
    summoner = Summoner.objects.order_by('-created_date')
    return render(request, 'lolsito/summoner_list.html', {'summoners':summoner})