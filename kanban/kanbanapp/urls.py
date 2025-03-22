from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import TableView, BlogView, SubTaskView

schema_view = get_schema_view(
    openapi.Info(
        title="Kanban Task Manager API",
        default_version="v1",
        description="API documentation for your Kanban Task Manager",
        terms_of_service="https://www.yoursite.com/terms/",
        contact=openapi.Contact(email="your@email.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]