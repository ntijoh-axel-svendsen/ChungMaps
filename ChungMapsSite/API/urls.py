from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('blocks/', views.MinecraftBlockList.as_view()),
    path('blocks/<int:pk>/', views.MinecraftBlockDetail.as_view()),
    path('blocks/<str:dimension>/', views.MinecraftBlockList.as_view()),
    path('blocks/<str:dimension>/<int:x>/<int:y>/<int:z>/', views.MinecraftBlockDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
