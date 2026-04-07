from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='star')

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Admitionwala IT Services")
    company_description = models.TextField(help_text="Company overview and mission")
    vision = models.TextField(help_text="Company vision statement")
    mission = models.TextField(help_text="Company mission statement")
    about_founder = models.TextField(help_text="Information about the founder")
    countries_served = models.CharField(max_length=100, default="India, UK, USA")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"
        verbose_name = "About Us"


class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('founder', 'Founder & CEO'),
        ('technical_lead', 'Technical Lead'),
        ('marketing_head', 'Marketing Head'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('manager', 'Project Manager'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    description = models.TextField(help_text="Team member bio and expertise")
    image = models.ImageField(upload_to='team/', blank=True, null=True, help_text="Profile picture")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter profile URL")
    order = models.IntegerField(default=0, help_text="Display order on page")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Team Members"
