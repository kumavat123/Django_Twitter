from . import views
from django.urls import path

urlpatterns = [
    path('', views.Twitter_List, name='Twitter_List'),
    path('create/', views.Twitter_create, name='Twitter_create'),
    path('<int:twitter_id>/delete/', views.Twitter_delete, name='Twitter_delete'),
    path('<int:twitter_id>/edit/', views.Twitter_edit, name='Twitter_edit'),
    path('register/', views.register, name='register'),
]
