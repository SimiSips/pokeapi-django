from django.urls import path
from core.views import berry, pokemon_detail, testView

urlpatterns = [
    path('test/', pokemon_detail, name='home'),
    path('berry/', berry, name='berry'),
    path('view/', testView.as_view(), name='testView')
]