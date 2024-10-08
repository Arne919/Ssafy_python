from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/score/', views.score, name='score'),
    path('my-score/', views.my_score, name='my_score'),

]
