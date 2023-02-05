from django.contrib import admin
from .models import Registration,Board,Duel

class RegisterAdmin(admin.ModelAdmin):
    readonly_fields = ('reg_time','last_round')
    list_display = ('id','name','email','phone','level')

class BoardAdmin(admin.ModelAdmin):
    list_display = ('boardno','location','busy')

class DuelAdmin(admin.ModelAdmin):
    readonly_fields = ('arbiter','start')

admin.site.register(Registration,RegisterAdmin)
admin.site.register(Board,BoardAdmin)
admin.site.register(Duel,DuelAdmin)