from django.shortcuts import render,redirect
from .models import Registration,Board,Duel,Annoucements
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

# user.groups.filter(name='Member').exists()

def is_member(user):
    return user.groups.filter(name='Manage Duel Staff').exists() or user.groups.filter(name='Arbiters').exists() or user.groups.filter(name='Registration Staff').exists() or user.is_superuser


def home(request):
    # View all options for registration,board,duel
    if is_member(request.user):
        return render(request,'index.html')
    return scoreboard(request)

def scoreboard(request):
    total = Registration.objects.all().count()
    waiting = Registration.objects.filter(waiting=True).count()
    alerts = Annoucements.objects.all().order_by('-id')
    live = []
    previous = []
    for lvl in range(1,11):
        duels = Duel.objects.filter(level=lvl,over=False).order_by('id')
        if len(duels)>0:
            live.append({'level':lvl,'duels':duels})
    for lvl in range(1,11):
        duels = Duel.objects.filter(level=lvl,over=True).order_by('id')
        if len(duels)>0:
            previous.append({'level':lvl,'duels':duels})
    return render(request,'scoreboard.html',{'live':live,'prev':previous,'total':total,'waiting':waiting,'alerts':alerts})


@staff_member_required(login_url='/user/loginpage/')
def registrations(request):
    regs = []
    for level in range(1,11):
        reg = Registration.objects.filter(level=level).order_by('-waiting','id')
        if not reg:
            continue
        regs.append({level:reg})
    return render(request,'registrations.html',{'registrations':regs})

@login_required(login_url='/user/loginpage/')
def newduelpage(request):
    if not request.user.groups.filter(name='Manage Duel Staff').exists() and not request.user.is_superuser:
        return HttpResponse("You are not valid to do this")
    free_boards = Board.objects.filter(busy=False)
    regs = []
    for level in range(1,11):
        reg = Registration.objects.filter(level=level,waiting=True).order_by('times_white_played')
        # rev_reg = Registration.objects.filter(level=level,waiting=True).order_by('-times_white_played')
        if not reg:
            continue
        regs.append({level:reg})
    return render(request,'newduel.html',{'boards':free_boards,'waitings':regs})

@login_required(login_url='/user/loginpage/')
def newduel(request):
    if not request.user.groups.filter(name='Manage Duel Staff').exists() and not request.user.is_superuser:
        return HttpResponse("You are not valid to do this")
    if request.method=="POST":
        boardid = request.POST['boardid']
        playerwhite = request.POST['playerwhite']
        playerblack = request.POST['playerblack']
        level = request.POST['level']
        board = ""
        try:
            board = Board.objects.get(id=boardid)
        except:
            return HttpResponse("Board not found")
        if board.busy == True:
            return HttpResponse("Board is Not Vacant Yet")
        player1 = ""
        player2 = ""
        try:
            player1 = Registration.objects.get(id=playerwhite)
        except:
            return HttpResponse("Player 1 not found")
        try:
            player2 = Registration.objects.get(id=playerblack)
        except:
            return HttpResponse("Player 2 not found")
        if player1.waiting == False:
            return HttpResponse("Player 1 is not in waiting list")
        if player2.waiting == False:
            return HttpResponse("Player 2 is not in waiting list")
        if player1.level != player2.level and player2.level != level:
            return HttpResponse("Player Are Not at Same Level. Contact Developer")
        Duel(board=board,player1=player1,player2=player2,level=level).save()
        player1.waiting = False
        player1.times_white_played += 1
        player1.save()
        player2.waiting = False
        player2.save()
        board.busy = True
        board.save()
        return redirect("/newduelpage/")
    else:
        return HttpResponse("Invalid Request - Not Secure")

@login_required(login_url='/user/loginpage/')
def duelwinpage(request):
    if not request.user.groups.filter(name='Arbiters').exists() and not request.user.is_superuser:
        return HttpResponse("You are not valid to do this")
    duels = Duel.objects.filter(over=False)
    return render(request,'duelwin.html',{'duels':duels})

@login_required(login_url='/user/loginpage/')
def duelwin(request,pk):
    if not request.user.groups.filter(name='Arbiters').exists() and not request.user.is_superuser:
        return HttpResponse("You are not valid to do this")
    duel = ""
    try:
        duel = Duel.objects.get(id=pk)
    except:
        return HttpResponse("No such Duel found.")
    winnerid = request.POST['winnerid']
    winner = ""
    try:
        winner = Registration.objects.get(id=winnerid)
    except:
        return HttpResponse("Winner is not registered")
    boardid = request.POST['boardid']
    board = ""
    try:
        board = Board.objects.get(id=boardid)
    except:
        return HttpResponse("No Board found for the game")
    duel.winner = winner
    duel.over = True
    duel.arbiter = request.user
    duel.save()
    winner.waiting = True
    winner.level = (winner.level + 1)
    winner.save()
    board.busy = False
    board.save()
    return redirect("/duelwinpage/")

@login_required(login_url='/user/loginpage/')
def allduels(request):
    live = Duel.objects.filter(over=False).order_by('id')
    previous = Duel.objects.filter(over=True).order_by('id')
    return render(request,'allduels.html',{'live':live,'prev':previous})