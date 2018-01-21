from django.conf.urls import url
from .views import CustomerList
urlpatterns = [
    url(r'^$', CustomerList.as_view(), name='home')
]