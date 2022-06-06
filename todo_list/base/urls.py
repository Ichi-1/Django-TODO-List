from django.urls import path
from .views import (
    TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteTask,
    CustomLogin, SingUpPage
)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', SingUpPage.as_view(), name='rootpage'),
    path('sign-up', SingUpPage.as_view(), name='sign-up'),
    path('login', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('task', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task-id'),
    path('task/create/', TaskCreate.as_view(), name='task-create'),
    path('task/update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task/delete/<int:pk>', DeleteTask.as_view(), name='task-delete')
]
