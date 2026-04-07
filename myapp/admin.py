from django.contrib import admin
from .models import Article, Service, AboutUs, TeamMember


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Company Information', {
            'fields': ('title', 'company_description', 'countries_served')
        }),
        ('Mission & Vision', {
            'fields': ('mission', 'vision')
        }),
        ('Leadership', {
            'fields': ('about_founder',)
        }),
    )
    readonly_fields = ('updated_at',)
    
    def has_add_permission(self, request):
        # Only allow one AboutUs record
        return not AboutUs.objects.exists()


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'is_active', 'order')
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('name', 'description', 'email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'image', 'role', 'email', 'phone')
        }),
        ('Professional Details', {
            'fields': ('description', 'linkedin_url', 'twitter_url')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
