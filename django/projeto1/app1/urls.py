from django.urls import path
from .views import paginateste, pagina_home, pagina_login
urlpatterns = [
    
    path('teste/', paginateste, name="create_user"),
    path('teste/home', pagina_home, name="home"),
    path('login', pagina_login, name="login")
]
