from django.conf.urls import url
from template_app import views
from django.urls import path

app_name='template_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]
