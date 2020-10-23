from django.conf.urls import url
from .views import index, index_template

urlpatterns = [
    url(r'^hello/', index),
    url(r'^hellot/', index_template)
]
