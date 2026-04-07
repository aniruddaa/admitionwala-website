from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    
    def ready(self):
        # Customize Django admin site
        from django.contrib import admin
        admin.site.site_header = "Admitionwala IT Services Admin Panel"
        admin.site.site_title = "Admitionwala IT Services"
        admin.site.index_title = "Welcome to Admitionwala IT Services Admin"
