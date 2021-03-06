"""kankara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from .views import DashboardView
from accounts.views import login_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_view, name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logout.html'),
        name='logout'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^reports/', include('reports.urls', namespace='reports')),
    url(r'^sale/', include('sales.urls', namespace='sales')),
    url(r'^customer/', include('customers.urls', namespace='customers')),
]

# not for production. do not do this in production!
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)