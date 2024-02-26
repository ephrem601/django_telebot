from django.urls import path 
from .views import chat_view, webhook

app_name = 'chatgpt'

urlpatterns =[
    path('', chat_view, name='chat_view'),
    path('webhook/', webhook, name='webhook'),
]