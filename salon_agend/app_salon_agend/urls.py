from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'agendamentos', views.AgendamentoViewSet)

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('horarios/', views.horarios, name='horarios'),
    path('api/', include(router.urls)),
]
