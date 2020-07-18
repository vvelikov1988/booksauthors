from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addbook', views.addbook),
    path('addauthor', views.addauthor),
    path('viewbook/<int:id>', views.viewbook),
    path('authors', views.author),
    path('viewbook/<int:book_id>/assignauthor', views.assignauthor),
    path('viewauthor/<int:author_id>', views.viewauthor),

]
