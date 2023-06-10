from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', obtain_auth_token),

]

# view из библиотеки rest_framework.authtoken для получения токена
