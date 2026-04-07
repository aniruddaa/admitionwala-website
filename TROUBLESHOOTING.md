# 🔧 TROUBLESHOOTING GUIDE

## Common Issues & Solutions

### ❌ Issue 1: Photos Not Showing on About Page

**Symptoms:**
- Photos uploaded but not appearing on `/about/` page  
- Blank spaces where photos should be  
- Broken image icons

**Causes & Solutions:**

```
1. PHOTO NOT MARKED ACTIVE
   └─ Go to: Admin → Team Members
      └─ Check: "Is Active" checkbox is ✓
         └─ Click: Save
         
2. WRONG IMAGE FORMAT
   └─ Supported: JPG, PNG, GIF
      └─ Try: Convert to JPG
         └─ Re-upload
         
3. IMAGE TOO LARGE
   └─ Max: 2MB recommended
      └─ Resize to: 500x500px
         └─ Re-upload smaller version
         
4. SERVER NOT RELOADED
   └─ Django should auto-reload
      └─ If not: Stop & restart server
         └─ python manage.py runserver
         
5. CACHE ISSUE
   └─ Hard refresh browser: Ctrl+Shift+R
      └─ Clear browser cache
         └─ Try private/incognito window
```

**Quick Fix Checklist:**
- [ ] Is Active = checked?
- [ ] Photo file < 2MB?
- [ ] Format = JPG or PNG?
- [ ] Did you click Save?
- [ ] Did you refresh the page?

---

### ❌ Issue 2: Colors Look Wrong

**Symptoms:**
- Colors different than shown in guide  
- Site looks faded or washed out  
- Old purple colors still showing

**Causes & Solutions:**

```
1. OLD STYLESHEET CACHED
   └─ Clear cache: Ctrl+Shift+Delete
      └─ Hard refresh: Ctrl+Shift+R
         └─ Wait 10 seconds
         
2. BASE.HTML NOT UPDATED
   └─ Check: static/css/style-new.css is linked
      └─ In base.html around line 20:
         └─ <link rel="stylesheet" href="...style-new.css">
         
3. STATIC FILES NOT COLLECTED
   └─ Run: python manage.py collectstatic
      └─ Then restart server
         
4. BROWSER EXTENSION BLOCKING CSS
   └─ Disable: Dark mode extension
      └─ Disable: Ad blocker
         └─ Try different browser
         
5. STYLE.CSS STILL ACTIVE
   └─ Rename: static/css/style.css → style-old.css
      └─ Restart server
```

**Quick Fix Checklist:**
- [ ] Cleared browser cache?
- [ ] Hard refresh (Ctrl+Shift+R)?
- [ ] Checked base.html links style-new.css?
- [ ] Any extensions overriding CSS?
- [ ] Tried different browser?

---

### ❌ Issue 3: Site Not Responsive on Mobile

**Symptoms:**
- Mobile layout broken  
- Text overlapping on phones  
- Horizontal scrolling  
- Buttons too small to tap

**Causes & Solutions:**

```
1. VIEWPORT META TAG MISSING
   └─ Check base.html has:
      └─ <meta name="viewport" content="width=device-width">
         └─ Restart server if missing
         
2. CSS NOT LOADED
   └─ Check: Console for CSS errors (F12)
      └─ Look for: 404 errors
         └─ File path might be wrong
         
3. OLD CSS STILL ACTIVE
   └─ Rename: static/css/style.css
      └─ Keep only: style-new.css
         └─ Hard refresh
         
4. BROWSER ZOOM
   └─ Reset zoom: Ctrl+0
      └─ Check: actual mobile size
         └─ Open DevTools: F12 → mobile icon
         
5. DEVICE-SPECIFIC ISSUE
   └─ Try: Different phone/tablet
      └─ Try: Chrome DevTools mobile mode
         └─ Try: Different mobile browser
```

**Quick Fix Checklist:**
- [ ] Meta viewport tag present?
- [ ] CSS file loading without errors?
- [ ] Browser zoom at 100%?
- [ ] Tested in DevTools mobile mode?
- [ ] No horizontal scrolling?

**Test Responsive Design:**
```
1. Press F12 (DevTools)
2. Click phone icon (Toggle device toolbar)
3. Select iPhone 12/13
4. Scroll up/down - no horizontal scroll
5. Buttons = tappable (50px min)
6. Text readable without zoom
```

---

### ❌ Issue 4: Admin Panel Won't Load

**Symptoms:**
- 404 error on `/admin/`  
- "Page not found"  
- Can't login  
- Admin disabled

**Causes & Solutions:**

```
1. ADMIN URL NOT CONFIGURED
   └─ Check myproject/urls.py
      └─ Should include: from django.contrib import admin
         └─ Should have: path('admin/', admin.site.urls),
            
2. ADMIN APP NOT INSTALLED
   └─ Check myproject/settings.py
      └─ INSTALLED_APPS should include: 'django.contrib.admin'
         
3. MIGRATIONS NOT RUN
   └─ Run: python manage.py migrate
      └─ Then: python manage.py runserver
         
4. SUPERUSER NOT CREATED
   └─ Run: python manage.py createsuperuser
      └─ Enter username, email, password
         └─ Try login again
         
5. SERVER NOT RUNNING
   └─ Is terminal showing: "Starting development server"?
      └─ If not: python manage.py runserver
         └─ Wait 5 seconds for server start
```

**Quick Fix Checklist:**
- [ ] Server running (look for "Starting development server")?
- [ ] migrations applied (python manage.py migrate)?
- [ ] superuser created (python manage.py createsuperuser)?
- [ ] Can access: http://localhost:8000/?
- [ ] Admin app in INSTALLED_APPS?

---

### ❌ Issue 5: Photos Upload But Don't Save

**Symptoms:**
- File selected, clicked save  
- No error message  
- But photo disappears  
- Can't find file in media folder

**Causes & Solutions:**

```
1. PILLOW NOT INSTALLED
   └─ Check: pip list | grep Pillow
      └─ Should show: Pillow 12.1.1+
      └─ If not: pip install Pillow
         └─ Restart server
         
2. MEDIA_ROOT NOT CONFIGURED
   └─ Check settings.py has:
      └─ MEDIA_URL = '/media/'
         └─ MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
         
3. MEDIA FOLDER DOESN'T EXIST
   └─ Should exist: C:\...\attractive_website\media\
      └─ And: media/team/ folder
      └─ If not: Create via terminal
         └─ mkdir media
         └─ mkdir media\team
         
4. PERMISSIONS ISSUE
   └─ Check: Folder readable/writable
      └─ Right-click → Properties → Security
         └─ Ensure: Your user has write access
         
5. FILE TOO LARGE
   └─ Max recommended: 2MB
      └─ Compress image first
      └─ Use online image compressor
```

**Quick Fix Checklist:**
- [ ] Pillow installed (pip list | grep Pillow)?
- [ ] media/ folder exists?
- [ ] media/team/ folder exists?
- [ ] MEDIA_ROOT configured?
- [ ] File < 2MB?

---

### ❌ Issue 6: Old Tailwind Styles Still Showing

**Symptoms:**
- Random colors/styling appearing  
- Classes like "bg-purple-600" showing  
- Tailwind CDN effects visible  
- New CSS not applying

**Root Cause:**
Old base.html still has Tailwind CDN link

**Solution:**

```
Open: templates/base.html

Find: <script src="https://cdn.tailwindcss.com"></script>
      or <link href="..." tailwindcss>

Delete: The entire line

Verify: Link to style-new.css exists:
        <link rel="stylesheet" href="{% static 'css/style-new.css' %}">

Save: base.html

Refresh: Browser (Ctrl+Shift+R)
```

**Quick Check:**
```
In base.html near <head>:

❌ <script src="https://cdn.tailwindcss.com"></script>  ← DELETE THIS

✅ <link rel="stylesheet" href="{% static 'css/style-new.css' %}">  ← KEEP THIS
```

---

### ❌ Issue 7: 500 Error on Contact Form

**Symptoms:**
- Form field shows red  
- "Something went wrong"  
- 500 error in console  
- Can't submit contact form

**Causes & Solutions:**

```
1. EMAIL NOT CONFIGURED
   └─ Check settings.py has EMAIL settings
      └─ For testing: EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
         └─ This prints email to console (no SMTP needed)
         
2. CSRF TOKEN MISSING
   └─ Check: Form has {% csrf_token %}
      └─ Should be inside <form> tag
      └─ If missing: Add it
         
3. FORM VALIDATION FAILING
   └─ Check: All required fields filled
      └─ Name, Email, Message all required
      └─ Email must be valid format
      
4. DATABASE ERROR
   └─ Check: Migrations applied
      └─ Run: python manage.py migrate
         └─ Restart server
         
5. CHECK TERMINAL FOR ERROR
   └─ Look at: Terminal where server running
      └─ Error message there explains issue
      └─ Copy error and search for solution
```

**Quick Fix Checklist:**
- [ ] All form fields filled?
- [ ] Email format valid?
- [ ] {% csrf_token %} in form?
- [ ] Database migrated?
- [ ] Check server terminal for error?

**For Testing Only (Remove Later):**
```python
# In settings.py - for development testing only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

---

### ❌ Issue 8: Static Files (CSS/JS) Not Loading

**Symptoms:**
- Browser console: "Failed to load stylesheet"  
- 404 errors for CSS/JS  
- Unstyled website  
- Colors/animations not working

**Causes & Solutions:**

```
1. WRONG STATIC TAG
   └─ Should be: {% load static %}
      └─ At TOP of template
      └─ Before using {% static '...' %}
         
2. WRONG FILE PATH
   └─ Check: Path is correct
      └─ Should be: {% static 'css/style-new.css' %}
      └─ NOT: {% static 'static/css/style-new.css' %}
      └─ NOT: {% static '/css/style-new.css' %}
         
3. SERVER NOT SERVING STATIC
   └─ In development: Should be auto
      └─ Check: DEBUG = True in settings.py
      └─ If False: Run: python manage.py collectstatic
         
4. FOLDER NOT CREATED
   └─ Check: static/ folder exists
      └─ Check: static/css/ folder exists
      └─ Check: style-new.css file in there
         
5. TYPO IN FILENAME
   └─ Check spelling: style-new.css
      └─ NOT: style_new.css
      └─ NOT: stylenew.css
      └─ Case-sensitive on Linux!
```

**Debug Command:**
```
Open browser F12 → Network tab
Refresh page
Look for red 404 errors
Click them to see:
- What path it tried
- Where it looked
- What exists instead
```

**Quick Fix Checklist:**
- [ ] {% load static %} at top of template?
- [ ] Using correct static tag syntax?
- [ ] File name spelled correctly?
- [ ] File actually exists in folder?
- [ ] Folder path correct (static/css/)?

---

### ❌ Issue 9: Database Locked Error

**Symptoms:**
- "database is locked"  
- Can't access admin  
- Server won't start  
- Django errors about sqlite3

**Solutions:**

```
1. CLOSE ALL CONNECTIONS
   └─ Stop server: Ctrl+C
      └─ Wait 5 seconds
      └─ Restart: python manage.py runserver
         
2. REMOVE LOCK FILE (if exists)
   └─ In folder: attractive_website/
      └─ Look for: db.sqlite3-journal
      └─ Delete it if present
      └─ Restart server
      
3. CLOSE MULTIPLE SERVERS
   └─ Only ONE server can access db.sqlite3
      └─ Check: Any other Terminal tabs running Django
      └─ Stop them all
      └─ Restart main server
      
4. RESTART VSCode
   └─ Close: All terminals
      └─ Close: VSCode
      └─ Reopen: VSCode
      └─ Start: Fresh server
      
5. BROWSER STILL ACCESSING
   └─ Close: Browser tabs with Django site
      └─ Restart: Server
      └─ Then: Open fresh browser tab
```

**Quick Fix:**
```
Terminal: Ctrl+C (stop server)
Wait: 5 seconds
Terminal: python manage.py runserver
Refresh: Browser page
```

---

### ❌ Issue 10: Team Members Not Showing in Order

**Symptoms:**
- Team members display randomly  
- Order field not working  
- Members showing out of sequence

**Solution:**

```
Go to: Admin → Team Members

For each member, set:
- Prof. Aniruddha: Order = 1
- Rajesh Kumar: Order = 2
- Priya Sharma: Order = 3

Also check:
- Is Active = ✓ (checked)
- Order = 1, 2, 3 (ascending)

Save each one.

Refresh: About page (Ctrl+Shift+R)

Should now display: 1, 2, 3 in order
```

---

## 🆘 When All Else Fails

### Nuclear Option (Safe Reset)

```
1. Stop server: Ctrl+C
2. Delete: db.sqlite3 (database)
3. Delete: media/team/* (all uploaded photos)
4. Run: python manage.py migrate
5. Run: python manage.py populate_data
6. Create new superuser: python manage.py createsuperuser
7. Start: python manage.py runserver
8. Re-upload: Photos

⚠️ Does NOT delete:
- Templates (still work)
- CSS/JS (still work)
- Settings (preserved)

✅ Fixes almost ALL issues
```

---

## 📞 Quick Reference: Common Commands

```bash
# Start server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Database migrations
python manage.py migrate

# Populate demo data
python manage.py populate_data

# Collect static files (production)
python manage.py collectstatic

# Shell (test code)
python manage.py shell

# Check for issues
python manage.py check

# See URL patterns
python manage.py show_urls
```

---

## 🔍 Debugging Your Django Project

### Enable Debug Mode
```python
# In settings.py
DEBUG = True  # See detailed error pages
ALLOWED_HOSTS = ['*']  # Allow all for development
```

### Check Terminal Output
```
When error occurs, look at terminal where server running:

[ERROR] ...
[WARNING] ...
[INFO] path to problem

Copy error → Google it → Solution usually there
```

### Use Django Shell
```bash
python manage.py shell

# Test imports
>>> from myapp.models import Service
>>> Service.objects.all()
<QuerySet [<Service: Web Development>, ...]>

# Exit
>>> exit()
```

---

## ⚡ Performance Tips

### Make Site Faster
```
1. Compress images before upload (< 1MB)
2. Use JPG for photos, PNG for icons
3. Consider CDN for images (later)
4. Enable browser caching
5. Minify CSS/JS (production)
```

---

## 🔐 Security Checklist

### Before Production
```
- [ ] DEBUG = False
- [ ] Set SECRET_KEY from environment
- [ ] Set secure ALLOWED_HOSTS
- [ ] Use HTTPS only
- [ ] Set SECURE_SSL_REDIRECT = True
- [ ] Secure cookies (session/csrf)
- [ ] Remove debug toolbar
- [ ] Check security issues
```

Command:
```bash
python manage.py check --deploy
```

---

## 📊 Verify Setup

### Confirmation Checklist
```bash
# These should all work:

# ✅ Server running
http://localhost:8000

# ✅ Home page
http://localhost:8000

# ✅ About page with team
http://localhost:8000/about/

# ✅ Portfolio
http://localhost:8000/portfolio/

# ✅ Contact form
http://localhost:8000/contact/

# ✅ Admin panel
http://localhost:8000/admin/
Login: your superuser credentials

# ✅ Django shell
python manage.py shell
>>> exit()

# ✅ Migrations done
python manage.py migrate --check

# ✅ No errors
python manage.py check
```

---

## 🆘 Still Stuck?

**Check in This Order:**
1. Look at this troubleshooting guide
2. Check terminal output (where server running)
3. Check browser console (F12 → Console tab)
4. Check Admin for model errors
5. Restart server (Ctrl+C, then python manage.py runserver)
6. Clear browser cache (Ctrl+Shift+Delete)
7. Try fresh browser tab
8. Restart VSCode entirely

**Most issues solved by:**
```
1. Restarting server
2. Clearing cache
3. Hard refresh (Ctrl+Shift+R)
4. In that order
```

---

**Remember:** The terminal where Django runs shows ALL errors. Start debugging there!

Happy coding! 🚀
