# Chisanga Kabwe - Portfolio Website

## Overview
A modern, professional portfolio website built with Django showcasing projects, skills, and professional experience. Features a sleek dark theme with gradient accents, smooth animations, and responsive design.

## Purpose
Display Chisanga Kabwe's software development work, technical skills, and provide a contact method for potential collaborations or opportunities.

## Current State
✅ **Fully functional** - Website is live with all features working
- Django backend serving dynamic content
- Modern, animated frontend with dark theme
- 6 featured projects displayed with screenshots
- 14 technical skills categorized by type
- Working contact form
- Django admin panel for content management

## Project Structure
```
portfolio_site/          # Django project settings
portfolio/              # Main application
  ├── models.py        # Project, Skill, ContactMessage models
  ├── views.py         # Home and project views
  ├── urls.py          # URL routing
  ├── admin.py         # Admin panel configuration
  ├── templates/       # HTML templates
  │   └── portfolio/
  │       ├── base.html
  │       └── home.html
  └── templatetags/    # Custom template filters
      └── portfolio_filters.py
static/                 # Static files
  ├── css/style.css   # Custom styles
  └── js/main.js      # JavaScript animations
media/                  # User-uploaded files
  └── projects/        # Project screenshots
```

## Key Features
1. **Hero Section** - Animated introduction with gradient text effects
2. **About Section** - Professional background and stats
3. **Projects Showcase** - Grid display with image overlays and tech stacks
4. **Skills Display** - Categorized skills with proficiency bars
5. **Contact Form** - Message submission with Django backend
6. **Admin Panel** - Easy content management at `/admin/`

## Technology Stack
- **Backend**: Django 5.2.7, Python 3.11
- **Frontend**: Bootstrap 5, AOS (Animate On Scroll)
- **Database**: SQLite (development)
- **Static Files**: WhiteNoise
- **Image Handling**: Pillow

## Featured Projects
1. Payroll Management System (Django, MySQL)
2. CUZ Attendance System (Django, PostgreSQL)
3. Cryotherapy Chatbot (Python, AI/ML)
4. Flight Seat Booking Simulator (Java, MySQL)
5. Note Taking App (JavaScript)
6. Cartoon Hero Website (HTML/CSS/JS)

## Skills Categories
- **Backend**: Python, Django, Java, Go
- **Frontend**: JavaScript, HTML/CSS, Bootstrap, React
- **Database**: MySQL, PostgreSQL, SQLite
- **Tools**: Git, Linux, Docker

## Admin Access
- URL: `/admin/`
- Admin account created - check console output or create a new superuser with `python manage.py createsuperuser`

## Recent Changes (October 22, 2025)
- Created complete Django portfolio website from scratch
- Extracted and organized project screenshots from user's zip file
- Implemented custom template filters for string manipulation
- Set up WhiteNoise for static file serving
- Added 6 projects with images and descriptions
- Added 14 technical skills with proficiency levels
- Configured Django admin for easy content management
- Applied modern dark theme with gradient accents
- Implemented smooth scroll animations with AOS library

## User Preferences
- Modern, cool-looking design with dark theme
- Gradient color scheme (purple/indigo)
- Smooth animations and transitions
- Professional presentation of work

## Architecture Decisions
- **WhiteNoise** for static file serving (simple deployment)
- **Custom template filters** for string operations in templates
- **Bootstrap 5** for responsive grid and components
- **AOS library** for scroll animations
- **Featured flag** on projects for homepage display
- **Category grouping** for skills organization

## Contact Information
- **GitHub**: https://github.com/chisangasage
- **LinkedIn**: https://www.linkedin.com/in/chisanga-k
- **Location**: Liaoning Province, Fushun City, China

## Notes
- Server runs on port 5000
- Media files are served from `/media/` in development
- Static files collected to `/staticfiles/` for production
- Sample data script included: `add_sample_data.py`
