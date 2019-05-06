from django.urls import path
from api import views
#
# urlpatterns = [
# 	path('task_lists/', views.task_lists),
# 	path('task_lists/<int:pk>/', views.task_lists_detail),
# 	path('task_lists/<int:pk>/tasks/', views.tasks)
# ]

urlpatterns = [
	path('task_lists/', views.TaskLists.as_view()),
	path('task_lists/<int:pk>/', views.TaskListDetail.as_view()),
	path('users/', views.UserList.as_view()),
	path('login/', views.login),
	path('logout/', views.logout),
	path('task_lists/<int:pk>/tasks/', views.Tasks.as_view())
]