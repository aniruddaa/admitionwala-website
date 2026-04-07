# AdditionWala Admin Panel Guide

## Quick Start

### 1. Create Superuser (First Time Setup)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account with email and password.

### 2. Access Admin Panel
- Navigate to: `http://localhost:8000/admin/`
- Login with your superuser credentials
- You'll see: **AdditionWala Admin Panel**

---

## Managing About Us

### Access About Us Section
1. Go to Admin Panel → **About Us**
2. Click on the existing "About AdditionWala IT & Marketing Services" entry (only one allowed)
3. Edit the following fields:

### About Us Fields:
- **Title**: Company name/title
- **Company Description**: Main company overview and mission statement
- **Vision**: Your company's vision statement
- **Mission**: Your company's mission statement
- **About Founder**: Biography and information about the founder
- **Countries Served**: Countries where the company operates (e.g., "India, UK, USA")

### Example Content:
```
Title: About AdditionWala IT & Marketing Services

Company Description:
AdditionWala is a Pune-based technology startup delivering world-class web development, 
digital marketing, data analytics, and application services globally. Founded on principles 
of innovation, quality, and customer success, we transform businesses through cutting-edge 
digital solutions.

Vision:
To be the most trusted technology and marketing partner for businesses seeking digital 
transformation and sustainable growth across India, UK, and USA.

Mission:
To deliver exceptional digital solutions that empower businesses to achieve their goals 
through innovation, expertise, and unwavering commitment to customer success.

About Founder:
Prof. Aniruddha Jadhav is the visionary founder and CEO of AdditionWala. With a background 
in technology and entrepreneurship, Prof. Jadhav brings over 15 years of experience...

Countries Served: India, UK, USA
```

---

## Managing Team Members

### Add Team Member
1. Go to Admin Panel → **Team Members**
2. Click **+ Add Team Member** button

### Team Member Fields:

#### Personal Information
- **Name**: Full name of team member
- **Role**: Select from dropdown:
  - Founder & CEO
  - Technical Lead
  - Marketing Head
  - Developer
  - Designer
  - Project Manager
  - Other
- **Image**: Upload profile picture (JPG/PNG)
- **Email**: Email address
- **Phone**: Contact phone number

#### Professional Details
- **Description**: Bio and expertise (50-100 words recommended)
- **LinkedIn URL**: Link to LinkedIn profile (e.g., https://linkedin.com/in/username)
- **Twitter URL**: Link to Twitter profile (e.g., https://twitter.com/username)

#### Display Settings
- **Order**: Number for display order (1, 2, 3, etc.) - Lower numbers appear first
- **Is Active**: Check to display on website, uncheck to hide

### Example Team Member:
```
Name: Prof. Aniruddha Jadhav
Role: Founder & CEO
Image: [Upload photo]
Email: aniruddha@additionwala.com
Phone: +91-9876543210
LinkedIn: https://linkedin.com/in/aniruddha-jadhav
Twitter: https://twitter.com/aniruddha
Description: Founder & CEO with 15+ years in technology leadership and digital transformation. 
Visionary entrepreneur driving innovation and company growth.
Order: 1
Is Active: ✓ Checked
```

### Edit Existing Team Member
1. Go to Admin Panel → **Team Members**
2. Click on the team member's name to edit
3. Make changes and click **Save**

### Delete Team Member
1. Go to Admin Panel → **Team Members**
2. Select team member(s) checkbox
3. Select "Delete selected team members" from action dropdown
4. Click **Go**

### Reorder Team Members
1. Go to Admin Panel → **Team Members**
2. Use the **Order** column to change display sequence
3. Click **Save** after making changes

---

## Managing Services

### Add Service
1. Go to Admin Panel → **Services**
2. Click **+ Add Service**
3. Fill in:
   - **Name**: Service name (e.g., "Web Development")
   - **Description**: Service description
   - **Icon**: Font Awesome icon name (e.g., "globe" for globe icon)

### Common Icons:
- `globe` - Web Development
- `chart-bar` - Digital Marketing
- `chart-line` - Data Analytics
- `mobile-alt` - Mobile Apps
- `brain` - AI/ML
- `rocket` - Innovation
- `shield-alt` - Security
- View more at: https://fontawesome.com/icons

---

## Managing Projects/Articles

### Add Project
1. Go to Admin Panel → **Articles**
2. Click **+ Add Article**
3. Fill in:
   - **Title**: Project/case study name
   - **Description**: Details about the project
   - **Image**: Project image (optional)

### Edit Project
1. Go to Admin Panel → **Articles**
2. Click on the article title
3. Make changes and click **Save**

### Sort Projects
Projects display in reverse chronological order (newest first).

---

## Default Login Credentials

After running `python manage.py createsuperuser`, you'll have:
- **Username**: [your chosen username]
- **Password**: [your chosen password]
- **Email**: [your email]

### Reset Password
If you forget the password, run:
```bash
python manage.py changepassword username
```

---

## Important Features

### Image Upload
- Supported formats: JPG, PNG, GIF, WebP
- Maximum size: No limit (recommended < 5MB)
- Images are stored in: `media/team/` (team photos) and `media/articles/` (project images)

### Only One About Us Record
- The system only allows one "About Us" entry
- You cannot add multiple - only edit the existing one
- This ensures consistency across the website

### Team Member Display
- Only members with **Is Active** checked appear on the website
- Order number controls position (1 = first, 2 = second, etc.)
- Display order can be changed without publishing

### Inline Editing
- You can edit the **Order** and **Is Active** fields directly in the list view
- No need to open each record individually

---

## Accessing Images on Website

After uploading team member images, they will automatically display on:
- **About Page** → Team member cards show uploaded images
- Admin URL format: `http://localhost:8000/media/team/[filename]`

---

## Troubleshooting

### Images Not Uploading
- Check file size (should be < 100MB)
- Ensure file format is JPG/PNG
- Check folder permissions on `media/` folder

### Team Members Not Showing
- Verify **Is Active** is checked ✓
- Check that members have an **Order** value set
- Refresh the website (Ctrl+F5)

### Admin Panel Not Accessible
- Ensure Django development server is running
- Check URL: `http://localhost:8000/admin/`
- Verify login credentials are correct

### Changes Not Appearing
- Click **Save** (not just fill forms)
- Refresh website browser (Ctrl+F5 to clear cache)
- Restart Django server if needed

---

## Admin Panel Navigation

| Section | Purpose |
|---------|---------|
| **About Us** | Manage company information and About page content |
| **Team Members** | Add/edit/delete team members with photos |
| **Services** | Manage service offerings and descriptions |
| **Articles** | Manage projects/case studies |
| **Users** | Manage admin user accounts |
| **Groups** | Manage permission groups |

---

## Live Website Display

Your changes appear immediately:
- `/` → Home page (shows services, projects, stats)
- `/portfolio/` → Portfolio page (shows all articles/projects)
- `/about/` → About page (shows company info + team members)
- `/contact/` → Contact page

---

## Next Steps

1. **Create Superuser** (if not already done):
   ```bash
   python manage.py createsuperuser
   ```

2. **Add Team Members**:
   - Go to Admin → Team Members
   - Add at least 3-5 team members with photos

3. **Customize About Us**:
   - Go to Admin → About Us
   - Update company description, mission, vision

4. **Upload Team Photos**:
   - Use Admin image upload for professional photos
   - Recommended: 500x500px JPG images

5. **Test on Website**:
   - Visit `/about/` to see your team
   - Visit `/` to see services

---

**Admin Panel URL**: http://localhost:8000/admin/

For questions or additional customization, refer to Django documentation or contact development team.
