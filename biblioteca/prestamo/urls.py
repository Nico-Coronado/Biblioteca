from django.urls import path

from . import views

app_name = 'loan_app'

urlpatterns = [
    path('lista-prestamos/', views.LoanListView.as_view(), name='loan-list'),
    path('detalle-prestamo/<pk>/', views.LoanDetailView.as_view(), name='detail-loan'),
]