from django.urls import path
from . import views

urlpatterns = [
    path('', views.folder_index, name='folder_index'),
    path('create/', views.create_folder_view, name='create_folder'),
    path('update/<int:folder_id>/', views.update_folder_view, name='update_folder'),
    path('delete/<int:folder_id>/', views.delete_folder_view, name='delete_folder'),
    path('<int:folder_id>/', views.folder_detail_view, name='folder_detail'),
]
