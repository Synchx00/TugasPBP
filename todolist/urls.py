from django.urls import path
from todolist.views import show_todolist, show_json, add_task
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import update_task
from todolist.views import delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('createtask/', create_task,  name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('update_task/<str:key>/', update_task, name='update_task'),
    path('delete_task/<str:key>/', delete_task, name="delete_task"),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task'),
]