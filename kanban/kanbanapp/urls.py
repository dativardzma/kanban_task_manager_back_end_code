from django.urls import path, include
from .views import TableView, BlogView, SubTaskView

urlpatterns = [
    path('table/create/', TableView.as_view(), name="create_table"),
    path('table/<int:pk>/delete', TableView.as_view(), name="delete_table"),
    path('table/<int:pk>/update', TableView.as_view(), name="update_table"),
    path('table/<int:pk>/', TableView.as_view(), name="read_table"),
    path('blog/create/', BlogView.as_view(), name='create_blog'),
    path('blog/<int:pk>/delete', BlogView.as_view(), name='delete_blog'),
    path('blog/<int:pk>/update', BlogView.as_view(), name='update_blog'),
    path('blog/<int:pk>/', BlogView.as_view(), name="read_blog"),
    path('subtask/create/', SubTaskView.as_view(), name='create_subtask'),
    path('subtask/<int:pk>/delete', SubTaskView.as_view(), name='delete_subtask'),
    path('subtask/<int:pk>/update', SubTaskView.as_view(), name='update_subtask'),
    path('subtask/<int:pk>/', SubTaskView.as_view(), name="read_subtask"),
]