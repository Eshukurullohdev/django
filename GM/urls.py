from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('submit/', collect_user_info, name='collect_user_info'),
    path('success/', lambda request: render(request, 'success.html'), name='success')
]