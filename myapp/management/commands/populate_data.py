from django.core.management.base import BaseCommand
from myapp.models import Service, Article, AboutUs, TeamMember


class Command(BaseCommand):
    help = 'Populate database with sample services, projects, about us, and team members'

    def handle(self, *args, **options):
        # Clear existing data
        Service.objects.all().delete()
        Article.objects.all().delete()
        AboutUs.objects.all().delete()
        TeamMember.objects.all().delete()

        # Create Services
        services_data = [
            {
                'name': 'Web Development',
                'description': 'Custom websites & web applications built with modern stacks. Responsive, SEO-optimised & blazing fast — from landing pages to full enterprise platforms.',
                'icon': 'globe'
            },
            {
                'name': 'Digital Marketing',
                'description': '360° digital marketing — SEO, Google Ads, social media campaigns & lead generation that converts. Measurable ROI, transparent reporting.',
                'icon': 'chart-bar'
            },
            {
                'name': 'Data Analytics',
                'description': 'Transform raw data into actionable business intelligence. Custom dashboards, automated reports & AI-powered insights for smarter decisions.',
                'icon': 'chart-line'
            },
            {
                'name': 'Application Services',
                'description': 'Mobile & web app development for Android, iOS & cross-platform. MVPs to enterprise-grade applications, built to scale and perform.',
                'icon': 'mobile-alt'
            },
        ]

        services = []
        for service in services_data:
            s = Service.objects.create(**service)
            services.append(s)
            self.stdout.write(self.style.SUCCESS(f'Created service: {s.name}'))

        # Create Sample Projects/Articles
        articles_data = [
            {
                'title': 'E-Commerce Platform for Fashion Retail',
                'description': 'Built a scalable e-commerce platform for a leading fashion retailer. Increased sales by 300% in 6 months with improved user experience and mobile optimization.'
            },
            {
                'title': 'Digital Marketing Campaign - Lead Generation',
                'description': 'Executed comprehensive digital marketing strategy generating 5000+ qualified leads. ROI increased by 450% with optimized Google Ads and social media campaigns.'
            },
            {
                'title': 'Business Intelligence Dashboard',
                'description': 'Developed custom BI dashboard for enterprise client. Real-time analytics reduced decision-making time by 70% and improved operational efficiency.'
            },
            {
                'title': 'Mobile Banking Application',
                'description': 'Launched secure mobile banking app for financial institution. 50,000+ active users with 99.9% uptime and advanced security features.'
            },
            {
                'title': 'SaaS Platform Launch',
                'description': 'Developed and launched complete SaaS platform from concept to production. Acquired 200+ corporate clients in first year with continuous feature updates.'
            },
            {
                'title': 'AI-Powered Customer Support System',
                'description': 'Implemented AI-powered chatbot and support system reducing support tickets by 65%. Improved customer satisfaction score from 3.2 to 4.7/5.0.'
            },
        ]

        for article in articles_data:
            a = Article.objects.create(**article)
            self.stdout.write(self.style.SUCCESS(f'Created article: {a.title}'))

        # Create About Us
        about_us_data = {
            'title': 'About Admitionwala IT Services',
            'company_description': 'Admitionwala IT Services is a Pune-based technology startup delivering world-class web development, digital marketing, data analytics, and application services globally. Founded on principles of innovation, quality, and customer success, we transform businesses through cutting-edge digital solutions.',
            'vision': 'To be the most trusted technology and marketing partner for businesses seeking digital transformation and sustainable growth across India, UK, and USA.',
            'mission': 'To deliver exceptional digital solutions that empower businesses to achieve their goals through innovation, expertise, and unwavering commitment to customer success.',
            'about_founder': 'Prof. Aniruddha Jadhav is the visionary founder and CEO of Admitionwala IT Services. With a background in technology and entrepreneurship, Prof. Jadhav brings over 15 years of experience in building scalable digital solutions and leading high-performing teams. His passion for innovation and customer satisfaction drives the company\'s mission to deliver world-class services.',
            'countries_served': 'India, UK, USA'
        }
        
        about_us = AboutUs.objects.create(**about_us_data)
        self.stdout.write(self.style.SUCCESS(f'Created About Us: {about_us.title}'))

        # Create Team Members
        team_members_data = [
            {
                'name': 'Prof. Aniruddha Jadhav',
                'role': 'founder',
                'description': 'Founder & CEO with 15+ years in technology leadership and digital transformation. Visionary entrepreneur driving innovation and company growth.',
                'email': 'aniruddha@admitionwala.com',
                'linkedin_url': 'https://linkedin.com/in/aniruddha-jadhav',
                'order': 1,
                'is_active': True
            },
            {
                'name': 'Rajesh Kumar',
                'role': 'technical_lead',
                'description': 'Chief Technology Officer with expertise in full-stack development, cloud architecture, and DevOps. Led 50+ successful projects with cutting-edge technology stack.',
                'email': 'rajesh@admitionwala.com',
                'linkedin_url': 'https://linkedin.com/in/rajesh-kumar',
                'order': 2,
                'is_active': True
            },
            {
                'name': 'Priya Sharma',
                'role': 'marketing_head',
                'description': 'Head of Digital Marketing & Business Development. 10+ years of experience in digital marketing strategy, SEO, and lead generation campaigns.',
                'email': 'priya@admitionwala.com',
                'linkedin_url': 'https://linkedin.com/in/priya-sharma',
                'order': 3,
                'is_active': True
            },
        ]

        for member in team_members_data:
            tm = TeamMember.objects.create(**member)
            self.stdout.write(self.style.SUCCESS(f'Created team member: {tm.name}'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
