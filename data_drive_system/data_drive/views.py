
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .raw_sql import create_folder, get_subfolders, update_folder_name, delete_folder_recursive
from .models import Folder

@login_required
def folder_index(request):
    folders = Folder.objects.filter(owner=request.user, parent=None)
    return render(request, 'accounts/data_drive/index.html', {'folders': folders})

@login_required
def create_folder_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        parent_id = request.POST.get('parent_id', None)
        create_folder(name, parent_id, request.user.id)
        return redirect('folder_index')
    return render(request, 'accounts/data_drive/create_folder.html')

@login_required
def update_folder_view(request, folder_id):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        update_folder_name(folder_id, new_name)
        return redirect('folder_index')
    folder = Folder.objects.get(id=folder_id)
    return render(request, 'accounts/data_drive/update_folder.html', {'folder': folder})

@login_required
def delete_folder_view(request, folder_id):
    delete_folder_recursive(folder_id)
    return redirect('folder_index')

@login_required
def folder_detail_view(request, folder_id):
    subfolders = get_subfolders(folder_id)
    return render(request, 'accounts/data_drive/detail.html', {'subfolders': subfolders})
