from django.shortcuts import render
from rest_framework import viewsets
from .models import Agendamento, Servico, Calendario
from .serializers import AgendamentoSerializer
from datetime import datetime
import calendar

def calendario(request):
    hoje = datetime.now()
    ano = hoje.year
    mes = hoje.month


    cal = calendar.Calendar(firstweekday=6) 
    dias_semana_num = cal.monthdayscalendar(ano, mes)
    
    nomes_meses = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    calendario_semanas = []
    for semana in dias_semana_num:
        semana_formatada = []
        for dia in semana:
            if dia == 0:
                semana_formatada.append({"dia": None})
            else:
                data_completa = datetime(ano, mes, dia)
                is_hoje = dia == hoje.day
                passado = data_completa.date() < hoje.date()
                
                semana_formatada.append({
                    "dia": dia,
                    "data_formatada": f"{ano}-{mes:02d}-{dia:02d}",
                    "bloqueado": passado,
                    "hoje": is_hoje
                })
        calendario_semanas.append(semana_formatada)

    context = {
        'mes_atual': nomes_meses[mes],
        'ano_atual': ano,
        'dias_da_semana': ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'],
        'calendario_semanas': calendario_semanas
    }
    return render(request, 'app_salon_agend/calendario.html', context)

def horarios(request):
    data_str = request.GET.get('data')
    
    data_selecionada = "Data Inválida"
    if data_str:
        try:
            data_obj = datetime.strptime(data_str, "%Y-%m-%d")
            data_selecionada = data_obj.strftime("%d/%m/%Y")
        except:
            pass
    servicos = Servico.objects.all()
    
    grade = ["07:00", "08:00", "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    horarios_list = []
    
    for h in grade:        
        horarios_list.append({
            "hora": h,
            "bloqueado": False 
        })

    context = {
        'data_selecionada': data_selecionada,
        'servicos': servicos,
        'horarios': horarios_list
    }
    return render(request, 'app_salon_agend/horarios_servicos.html', context)

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer