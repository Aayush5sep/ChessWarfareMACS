from django.db import models

class Registration(models.Model):
    name = models.CharField("Participant Name",max_length=40)
    email = models.EmailField("Participant Email",unique=True)
    phone = models.CharField("Participant Contact",max_length=10,unique=True)

    level = models.IntegerField("Round Number Qualified For",default=1)
    waiting = models.BooleanField("In Waiting?",default=True)

    reg_time = models.DateTimeField("Registration Time",auto_now_add=True)
    last_round = models.DateTimeField("Time Of Last Round Played",auto_now=True)

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
    arbiter = models.CharField(max_length=40,null=True,blank=True)
    level = models.IntegerField(default=1)
    start = models.DateTimeField("Starting Time",auto_now_add=True)
    over = models.BooleanField("Duel Over?",default=False)

    def __str__(self):
        return "Board " + str(self.board.boardno) + " : " + self.player1.name + " v/s " + self.player2.name