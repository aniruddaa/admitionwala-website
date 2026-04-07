from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__, static_folder='static', static_url_path='/static')

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "db.sqlite3")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'media')

# Create upload folders
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'articles'), exist_ok=True)
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'team'), exist_ok=True)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import models after db initialization
from models import create_models
Article, Service, AboutUs, TeamMember = create_models(db)

# Initialize Flask-Admin
admin = Admin(app, name='Admitionwala Admin')

# Add model views to admin
class ArticleAdmin(ModelView):
    column_list = ('title', 'created_at', 'updated_at')
    column_searchable_list = ('title', 'description')
    column_filters = ('created_at',)
    form_columns = ('title', 'description', 'image')

class ServiceAdmin(ModelView):
    column_list = ('name', 'icon')
    column_searchable_list = ('name',)

class TeamMemberAdmin(ModelView):
    column_list = ('name', 'role', 'email', 'is_active', 'order')
    column_searchable_list = ('name', 'email')
    column_filters = ('role', 'is_active')
    form_columns = ('name', 'role', 'description', 'image', 'email', 'phone', 'linkedin_url', 'twitter_url', 'order', 'is_active')

class AboutUsAdmin(ModelView):
    form_columns = ('title', 'company_description', 'vision', 'mission', 'about_founder', 'countries_served')

admin.add_view(ArticleAdmin(Article, db.session))
admin.add_view(ServiceAdmin(Service, db.session))
admin.add_view(TeamMemberAdmin(TeamMember, db.session))
admin.add_view(AboutUsAdmin(AboutUs, db.session))


# Serve media files
@app.route('/media/<path:filename>')
def serve_media(filename):
    """Serve media files from the media directory"""
    from werkzeug.security import safe_str_cmp
    try:
        media_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # Verify the file exists before serving
        if os.path.exists(media_path) and os.path.isfile(media_path):
            return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
        else:
            return {'error': 'File not found'}, 404
    except Exception as e:
        return {'error': str(e)}, 500


# Routes
@app.route('/')
def home():
    """Home page with hero section and services"""
    articles = Article.query.limit(6).all()
    services = Service.query.all()
    
    return render_template('home.html', 
                         articles=articles,
                         services=services,
                         page_title='Home - Admitionwala IT Services')


@app.route('/about/')
def about():
    """About page with company info and team members"""
    about_us = AboutUs.query.first()
    
    if not about_us:
        # Create default if doesn't exist
        about_us = AboutUs(
            title='About Admitionwala IT Services',
            company_description='Welcome to Admitionwala IT Services!',
            vision='To be the most trusted technology partner',
            mission='To deliver exceptional digital solutions',
            about_founder='Meet our founder Aniruddha Jadhav'
        )
        db.session.add(about_us)
        db.session.commit()
    
    team_members = TeamMember.query.filter_by(is_active=True).order_by(TeamMember.order).all()
    
    return render_template('about.html',
                         page_title='About Us',
                         about_us=about_us,
                         team_members=team_members)


@app.route('/portfolio/')
def portfolio():
    """Portfolio page showing all articles"""
    articles = Article.query.all()
    
    return render_template('portfolio.html',
                         articles=articles,
                         page_title='Portfolio')


@app.route('/contact/')
def contact():
    """Contact page"""
    return render_template('contact.html',
                         page_title='Contact')


@app.route('/careers/')
def careers():
    """Careers page with open positions"""
    return render_template('careers.html',
                         page_title='Careers')


@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if name and email and message:
            # Here you can add email sending logic or save to database
            return jsonify({
                'status': 'success',
                'message': 'Thank you! Your message has been sent successfully.'
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Please fill in all fields.'
            }), 400
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.context_processor
def utility_processor():
    """Make utility functions available in templates"""
    return dict(
        current_year=datetime.now().year
    )


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, host='127.0.0.1', port=8000)
