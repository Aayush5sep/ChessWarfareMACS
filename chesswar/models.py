from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    name = models.CharField("Participant Name",max_length=40)
    email = models.EmailField("Participant Email",unique=True,null=True,blank=True)
    phone = models.CharField("Participant Contact",max_length=10,unique=True)

    level = models.IntegerField("Round Number Qualified For",default=1)
    waiting = models.BooleanField("In Waiting?",default=True)

    reg_time = models.DateTimeField("Registration Time",auto_now_add=True)
    last_round = models.DateTimeField("Time Of Last Round Played",auto_now=True)

    times_white_played = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)+ ") " + self.name


class Board(models.Model):
    boardno = models.IntegerField("Board Number",default=0)
    location = models.CharField("Board Location",max_length=100,null=True,blank=True)
    busy = models.BooleanField("Match Live On Board?",default=False)

    def __str__(self):
        return str(self.boardno)


class Duel(models.Model):
    board = models.ForeignKey(Board,on_delete=models.DO_NOTHING,verbose_name="Board Number")
    player1 = models.ForeignKey(Registration,on_delete=models.DO_NOTHING,verbose_name="Player-White-Piece",related_name="PlayerWhitePiece")
    player2 = models.ForeignKey(Registration,on_delete=models.DO_NOTHING,verbose_name="Player-Black-Piece",related_name="PlayerBlackPiece")
    winner = models.ForeignKey(Registration,on_delete=models.DO_NOTHING,verbose_name="Board Winner",related_name="BoardWinner",null=True,blank=True)
    arbiter = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="Arbiter Name",null=True,blank=True)
    level = models.IntegerField(default=1)
    start = models.DateTimeField("Starting Time",auto_now_add=True)
    over = models.BooleanField("Duel Over?",default=False)

    def __str__(self):
        return "Board " + str(self.board.boardno) + " : " + self.player1.name + " v/s " + self.player2.name
    
class Annoucements(models.Model):
    message = models.TextField()
    warning_alert = models.BooleanField(default=False)
    danger_alert = models.BooleanField(default=False)
    success_alert = models.BooleanField(default=False)

    def ___str__(self):
        return self.message[20]