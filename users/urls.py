from django.urls import path

from users.views import CreateUserAPIView, UpdateUserAPIView, DestroyUserAPIView

app_name = 'users'

urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateUserAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', DestroyUserAPIView.as_view(), name='delete'),
]
