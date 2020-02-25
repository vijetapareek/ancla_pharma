from django.urls import path
from pharmapp import views

urlpatterns = [
   path(r'', views.pharmapp_view),
   path(r'pharma_website.html', views.pharmapp_view),
]