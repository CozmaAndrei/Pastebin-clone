from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), # url-ul pentru pagina home.html
    path('text/<int:id>/', views.full_text, name='full_text'), # url-ul pentru pagina text.html
    ]