from django.urls import path
from .views import home, detail, delete, update, create

app_name = 'adoption'

urlpatterns = [
    path('', home, name='home'),
    path('dog/<int:dog_id>/', detail, name='detail'),
    path('dog/<int:dog_id>/delete/', delete, name='delete'),
    path('dog/<int:dog_id>/update/', update, name='update'),
    path('create/', create, name='create')
]