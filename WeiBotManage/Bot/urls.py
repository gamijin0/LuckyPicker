from django.conf.urls import include, url
from .views import *


urlpatterns = [
    url(r'^manage',view=manage,name="botManage"),
    url(r'^addBot',view=addBot,name='addBot'),
]
