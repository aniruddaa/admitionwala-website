from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superadmin user for the admitionwala website'

    def handle(self, *args, **options):
        # Check if admin user already exists
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.WARNING('Superadmin user already exists!'))
            return

        # Create superadmin
        User.objects.create_superuser('admin', 'admin@admitionwala.com', 'admin@2026')
        
        self.stdout.write(self.style.SUCCESS('✓ Superadmin account created successfully!'))
        self.stdout.write(self.style.SUCCESS(''))
        self.stdout.write(self.style.WARNING('═' * 70))
        self.stdout.write(self.style.WARNING('SUPERADMIN CREDENTIALS'))
        self.stdout.write(self.style.WARNING('═' * 70))
        self.stdout.write(self.style.SUCCESS('Username: admin'))
        self.stdout.write(self.style.SUCCESS('Email: admin@admitionwala.com'))
        self.stdout.write(self.style.SUCCESS('Password: admin@2026'))
        self.stdout.write(self.style.WARNING('═' * 70))
        self.stdout.write(self.style.SUCCESS(''))
        self.stdout.write(self.style.WARNING('🔗 Access Admin Panel at: http://127.0.0.1:8000/admin/'))
        self.stdout.write(self.style.WARNING(''))
        self.stdout.write(self.style.WARNING('📝 Steps to Add Team Members:'))
        self.stdout.write(self.style.WARNING('1. Login to admin panel with above credentials'))
        self.stdout.write(self.style.WARNING('2. Go to "Team Members" section'))
        self.stdout.write(self.style.WARNING('3. Click "Add Team Member" button'))
        self.stdout.write(self.style.WARNING('4. Fill in the form with member details'))
        self.stdout.write(self.style.WARNING('5. Click "Save" to add the member'))
        self.stdout.write(self.style.WARNING(''))
