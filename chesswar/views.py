from django.shortcuts import render,redirect
from .models import Registration,Board,Duel
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

# user.groups.filter(name='Member').exists()

@login_required(login_url='/admin/')
def home(request):
    # View all options for registration,board,duel
    return render(request,'index.html')


@staff_member_required(login_url='/admin/')
def registrations(request):
    regs = []
    for level in range(1,11):
        reg = Registration.objects.filter(level=level).order_by('waiting','id')
        if not reg:
            continue
        regs.append({level:reg})
    return render(request,'registrations.html',{'registrations':regs})

@staff_member_required(login_url='/admin/')
def newduelpage(request):
    free_boards = Board.objects.filter(busy=False)
    regs = []
    for level in range(1,11):
        reg = Registration.objects.filter(level=level,waiting=True).order_by('id')
        if not reg:
            continue
        regs.append({level:reg})
    return render(request,'newduel.html',{'boards':free_boards,'waitings':regs})

@staff_member_required(login_url='/admin/')
def newduel(request):
    if not request.user.groups.filter(name='Manage Duel Staff').exists() and not request.user.is_superuser:
        return HttpResponse("You are not valid to do this")
    if request.method=="POST":
        arbiter = request.POST['arbiter']
        boardid = request.POST['boardid']
        playerwhite = request.POST['playerwhite']
        playerblack = request.POST['playerblack']
        level = request.POST['level']
        board = ""
        try:
            board = Board.objects.get(id=boardid)
        except:
            return HttpResponse("Board not found")
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
        if board.busy == True:
            return HttpResponse("Board is Not Vacant Yet")
        Duel(arbiter=arbiter,board=board,player1=player1,player2=player2,level=level).save()
        player1.waiting = False
        player1.save()
        player2.waiting = False
        player2.save()
        board.busy = True
        board.save()
        return redirect("/newduelpage/")
    else:
        return HttpResponse("Invalid Request - Not Secure")

@staff_member_required(login_url='/admin/')
def duelwinpage(request):
    duels = Duel.objects.filter(over=False)
    return render(request,'duelwin.html',{'duels':duels})

@staff_member_required(login_url='/admin/')
def duelwin(request,pk):
    if not request.user.groups.filter(name='Arbiters').exists():
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
        return HttpResponse("Requested Winner not registered")
    boardid = request.POST['boardid']
    board = ""
    try:
        board = Board.objects.get(id=boardid)
    except:
        return HttpResponse("No Board Found for the game")
    duel.winner = winner
    duel.over = True
    duel.save()
    board.busy = False
    board.save()
    winner.waiting = True
    winner.level = winner.level+1
    winner.save()
    return redirect("/duelwinpage/")

@staff_member_required(login_url='/admin/')
def allduels(request):
    live = Duel.objects.filter(over=False).order_by('id')
    previous = Duel.objects.filter(over=True).order_by('id')
    return render(request,'allduels.html',{'live':live,'prev':previous})