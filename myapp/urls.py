from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('api/submit-contact/', views.submit_contact, name='submit_contact'),
    path('api/generate-demo/', views.generate_site_demo, name='generate_site_demo'),
    path('api/download-demo/', views.download_demo_zip, name='download_demo_zip'),
]
