from django.urls import path
from codegnanapp.views import Index, PostCreate, details,like

app_name = 'codegnanapp'

urlpatterns = [
    path('', Index, name='index'),
    path('create/', PostCreate.as_view(), name='create'),
    path('details/<int:pk>', details, name='details'),
    path('ajax/likes/', like, name='like'),
]
