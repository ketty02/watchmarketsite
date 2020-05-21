from django.urls import path
from users.views import register, handle_login, handle_logout, profile, upload

app_name = 'users'

urlpatterns = [
    path('login/', view=handle_login, name='login'),
    path('logout/', view=handle_logout, name='logout'),
    path('profile/', view=profile, name='profile'),
    path('register/', view=register, name='register'),
    path('upload/', view=upload, name='upload'),
]