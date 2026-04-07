from django.shortcuts import render
from django.http import JsonResponse
from .models import Article, Service, AboutUs, TeamMember
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from .site_generator import SiteArchitect
import io
import zipfile
from django.http import HttpResponse, FileResponse


def home(request):
    """Home page with hero section and services"""
    articles = Article.objects.all()[:6]
    services = Service.objects.all()
    
    context = {
        'articles': articles,
        'services': services,
        'page_title': 'Home - Attractive Website',
    }
    return render(request, 'home.html', context)


def about(request):
    """About page with company info and team members"""
    about_us = AboutUs.objects.first()
    team_members = TeamMember.objects.filter(is_active=True).order_by('order')
    
    if not about_us:
        # Create default if doesn't exist
        about_us = AboutUs.objects.create(
            title='About Admitionwala IT Services',
            company_description='Welcome to Admitionwala IT Services!',
            vision='To be the most trusted technology partner',
            mission='To deliver exceptional digital solutions',
            about_founder='Meet our founder Prof. Aniruddha Jadhav'
        )
    
    context = {
        'page_title': 'About Us',
        'about_us': about_us,
        'team_members': team_members,
    }
    return render(request, 'about.html', context)


def portfolio(request):
    """Portfolio page showing all articles"""
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'page_title': 'Portfolio',
    }
    return render(request, 'portfolio.html', context)


def contact(request):
    """Contact page"""
    context = {
        'page_title': 'Contact',
        'csrf_token': get_token(request),
    }
    return render(request, 'contact.html', context)


def careers(request):
    """Careers page with open positions"""
    context = {
        'page_title': 'Careers',
    }
    return render(request, 'careers.html', context)


@require_http_methods(["POST"])
def submit_contact(request):
    """Handle contact form submission"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if name and email and message:
            # Here you can add email sending logic or save to database
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you! Your message has been sent successfully.'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Please fill in all fields.'
            }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def generate_site_demo(request):
    """AI Site Architect 2.0: Multi-File Website Synthesis"""
    try:
        data = json.loads(request.body)
        prompt = data.get('prompt', '')
        
        if not prompt:
            return JsonResponse({'error': 'No prompt provided'}, status=400)
            
        architect = SiteArchitect(prompt)
        manifest = architect.generate_manifest()
        
        # Store for download view
        request.session['last_manifest'] = manifest['files']
        
        return JsonResponse({
            'status': 'success',
            'pitch': manifest['pitch'],
            'html': manifest['files']['index.html'],
            'message': 'Full AI Synthesis Complete. Multi-file architecture ready.'
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def download_demo_zip(request):
    """Packages the last synthesized site into a ZIP archive"""
    manifest_files = request.session.get('last_manifest')
    if not manifest_files:
        return HttpResponse("No project has been synthesized in this session.", status=404)
        
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for filename, content in manifest_files.items():
            zf.writestr(filename, content)
            
    memory_file.seek(0)
    response = HttpResponse(memory_file, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="admitionwala-ai-synthesized-project.zip"'
    return response
