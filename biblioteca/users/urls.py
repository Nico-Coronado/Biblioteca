from django.urls import path
from . import views


app_name = 'user_app'

urlpatterns = [
    path('registro/', views.UserRegisterFormView.as_view(), name='register'),
    path('iniciar-sesion/', views.LoginUserView.as_view(), name='login'),
    path('cerrar-sesion/', views.LogoutView.as_view(), name='logout'),
]