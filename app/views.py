from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Player
from .forms import PlayerAddForm
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def Home(request):
    form=PlayerAddForm()
    players=Player.objects.all()
    context={
        'form':form,
        'players':players
    }
    return render(request,'app/home.html',context)

# @csrf_exempt
def Save_Data(request):
    if request.method=="POST":
        form=PlayerAddForm(request.POST)

        if form.is_valid():
            id = request.POST.get('playerid')
            if id == '':
                form.save()
            else:
                form=Player(id=id,
                            first_name=request.POST.get('first_name'),
                            middle_name=request.POST.get('middle_name'),
                            last_name=request.POST.get('last_name'),
                            country=request.POST.get('country'),
                            club=request.POST.get('club'))
                form.save()
            players=Player.objects.values()
            player_lst=list(players)
            print("Form Validation Sucessfull")
            return JsonResponse({'status':'Save','player_data':player_lst})
        else:
            print("Form Validation Failed")
            return JsonResponse({'status':'Failed'})

def Delete_Data(request):
    if request.method=="POST":
        id=request.POST.get('playerid')
        print(id)
        player=Player.objects.get(id=id)
        player.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def Edit_Data(request):
    if request.method=="POST":
        id=request.POST.get('playerid')
        print(id)
        player=Player.objects.get(id=id)
        playerinfo={'id':player.id,
                    'firstname':player.first_name,
                    'middlename':player.middle_name,
                    'lastname':player.last_name,
                    'country':player.country,
                    'club':player.club}
        return JsonResponse(playerinfo)
    else:
        return JsonResponse({'status':0})