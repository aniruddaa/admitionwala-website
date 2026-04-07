# AdditionWala IT & Marketing Services

A professional, modern website for AdditionWala IT & Marketing Services - a Pune-based technology startup delivering world-class web development, digital marketing, data analytics & application services globally.

## Features

- **Django Backend**: Full-featured Django application with models, views, and admin panel
- **Responsive Design**: Mobile-first approach with Tailwind CSS for beautiful styling
- **jQuery Interactions**: Smooth animations and interactive elements
- **Professional Branding**: AdditionWala branding with founder profile
- **Services Showcase**: Web Development, Digital Marketing, Data Analytics, Application Services
- **Stats Dashboard**: Real-time statistics with animated counters
- **Contact Management**: Fully functional contact form with AJAX submission
- **Admin Panel**: Manage projects and services through Django admin

## Tech Stack

- **Backend**: Django 4.2.0, Python 3.8+
- **Frontend**: Tailwind CSS 3, jQuery 3.6.0, Font Awesome 6.4.0
- **Database**: SQLite (development)
- **Animations**: CSS3 + jQuery

## Installation

1. **Extract the project folder**
   ```bash
   cd attractive_website
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://localhost:8000` to view the website.

## Project Structure

```
attractive_website/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── myproject/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/                  # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── templates/              # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── portfolio.html
│   ├── contact.html
│   ├── navbar.html
│   └── footer.html
└── static/                 # CSS, JS, Images
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── images/
```

## Pages

### Home
- Hero section with founder profile (Prof. Aniruddha Jadhav)
- "NOW ACCEPTING UK & US CLIENTS" announcement
- Core Services: Web Development, Digital Marketing, Data Analytics, Application Services
- Statistics: Projects, Services, Countries Served
- Featured projects showcase
- Call-to-action section

### About
- Company overview and mission
- "A Startup Built on Technology & Ambition"
- Service areas: UK, US, India
- Core values and differentiators
- Leadership team showcase

### Portfolio  
- Project gallery with filtering
- Case studies from satisfied clients
- Statistics dashboard
- Project categories

### Contact
- Contact form with validation
- Company information
- Location and service areas
- AJAX form submission

## Core Services

### 1. Web Development
- Custom websites & web applications
- React, Node.js, WordPress, E-Commerce
- Responsive, SEO-optimized, fast-loading
- From landing pages to enterprise platforms

### 2. Digital Marketing
- 360° digital marketing solutions
- SEO, Google Ads, Social Media campaigns
- Lead generation and conversion optimization
- Measurable ROI with transparent reporting

### 3. Data Analytics
- Transform raw data into actionable insights
- Custom dashboards and automated reports
- Power BI, Python, Machine Learning
- AI-powered business intelligence

### 4. Application Services
- Mobile & web app development
- Android, iOS, Flutter, PWA development
- MVPs to enterprise-grade applications
- Built to scale and perform

## Admin Access

- URL: `http://localhost:8000/admin`
- Username: (created during superuser setup)
- Password: (created during superuser setup)

### Adding Content

1. **Add Services**:
   - Navigate to Django admin
   - Add services under "Services"
   - Include name, description, and technology stack

2. **Add Projects**:
   - Add articles/projects under "Articles"
   - Include title, description, and dates
   - Projects automatically appear in portfolio

3. **Add Team Members**:
   - Customize team section in templates
   - Update founder information

## Company Information

**AdditionWala IT & Marketing Services**
- **Headquarter**: Pune, Maharashtra, India
- **Services**: Web Development, Digital Marketing, Data Analytics, Application Development
- **Serving**: UK, US, India
- **Founder & CEO**: Prof. Aniruddha Jadhav

## Key Features

✅ Animated gradient backgrounds
✅ Responsive design (Mobile, Tablet, Desktop)
✅ Professional color scheme (Dark navy, purple, yellow accents)
✅ jQuery smooth animations and interactions
✅ AJAX contact form with validation
✅ Portfolio filter functionality
✅ Animated statistics counters
✅ Founder profile card
✅ Technology tags for services
✅ Admin panel for content management

## Performance Optimizations

- Lazy loading for images
- CDN for external libraries (Tailwind, jQuery, Font Awesome)
- Minified CSS and JavaScript
- Optimized animations with CSS3
- Efficient jQuery selectors

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Future Enhancements

- [ ] Blog functionality
- [ ] Case study testimonials
- [ ] Live chat integration
- [ ] Email notification system
- [ ] SEO optimization tools
- [ ] Analytics integration
- [ ] Dark mode support
- [ ] Multi-language support

## Customization

### Change Colors
Edit `static/css/style.css` to modify gradient colors and theme colors.

### Update Company Info
- Home: Edit hero section in `templates/home.html`
- About: Update company details in `templates/about.html`
- Footer: Edit `templates/footer.html`

### Add/Edit Services
- Use Django admin at `/admin`
- Create new Service records
- Services automatically appear on homepage

## API Endpoints

### POST /api/submit-contact/
Submit contact form submission

**Request:**
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Your message here"
}
```

**Response:**
```json
{
    "status": "success",
    "message": "Thank you! Your message has been sent successfully."
}
```

## Support

For questions or support regarding this website, please contact:
**Email**: contact@additionwala.com

## License

This project is proprietary and created for AdditionWala IT & Marketing Services.

## Version

Version 1.0 - 2026

