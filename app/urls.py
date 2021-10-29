
from django.urls import path

from app.views import index, create, delete, edit

urlpatterns = [
    path('', index),
    path('create', create),
    path('delete/<int:id>', delete),
    path('edit/<int:id>', edit)
]
