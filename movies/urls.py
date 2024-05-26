from django.urls import path, include #Configurar urls para dirigir
from . import views #Importación de las vistas creadas
from django.contrib.auth import views as auth_views

#urls a direccionar
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("your_name/", views.get_name, name="get_name"),
    path("<int:movie_id>/review/", views.get_review, name="get_review"),
    path("login/", views.user_login, name="login"),
    path('register/', views.register_view, name='register'),  # URL para el registro
    path("logout/", views.user_logout, name="logout"),
    path('login/', views.get_return, name='get_return') #para regresar
]