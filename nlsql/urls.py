from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/',views.webhookTest.as_view(),name='webhook'),
]
