from django.contrib import admin
from .models import Servico, Agendamento, DiaBloqueado

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'hora', 'servico', 'telefone')
    list_filter = ('data', 'servico')
    search_fields = ('nome', 'telefone')

@admin.register(DiaBloqueado)
class DiaBloqueadoAdmin(admin.ModelAdmin):
    list_display = ('data', 'motivo')
