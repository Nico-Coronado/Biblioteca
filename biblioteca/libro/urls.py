from django.urls import path

from . import views

app_name = 'book_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('lista-libros/', views.BookListView.as_view(), name='list-book'),
    path('detalle-libro/<pk>/', views.BookDetailView.as_view(), name='detail-book'),
]