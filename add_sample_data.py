import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from portfolio.models import Project, Skill

Project.objects.all().delete()
#Skill.objects.all().delete()

projects_data = [
    {
        'title': 'Payroll Management System',
        'description': 'A comprehensive payroll management system built with Django and MySQL. Features include employee management, salary calculations, tax deductions, payslip generation, and detailed reporting.',
        'tech_stack': 'Python, Django, MySQL, Bootstrap',
        'github_link': 'https://github.com/chisangasage/payroll_system',
        'image': 'projects/Screenshot from 2025-10-22 13-51-19.png',
        'featured': True,
        'order': 1,
    },
    {
        'title': 'CUZ Attendance System',
        'description': 'An intelligent attendance tracking system for educational institutions. Provides real-time attendance monitoring, automated reporting, and student performance analytics.',
        'tech_stack': 'Python, Django, PostgreSQL, JavaScript',
        'image': 'projects/Screenshot from 2025-10-08 10-52-03.png',
        'featured': True,
        'order': 2,
    },
    {
        'title': 'Cryotherapy Chatbot',
        'description': 'An AI-powered chatbot designed to provide information about cryotherapy treatments. Features natural language processing and intelligent responses to user queries.',
        'tech_stack': 'Python, AI/ML, Django, NLP',
        'image': 'projects/Screenshot from 2025-10-22 13-56-42.png',
        'featured': True,
        'order': 3,
    },
    {
        'title': 'Flight Seat Booking Simulator',
        'description': 'A Java-based flight seat booking system with a graphical user interface and MySQL database integration. Allows users to book, modify, and cancel flight reservations.',
        'tech_stack': 'Java, MySQL, Swing GUI',
        'github_link': 'https://github.com/chisangasage/FlightSeatBookingSimulator',
        'featured': True,
        'order': 4,
    },
    {
        'title': 'Note Taking App',
        'description': 'A simple yet powerful note-taking application with rich text editing, categorization, and search functionality.',
        'tech_stack': 'JavaScript, HTML, CSS, LocalStorage',
        'github_link': 'https://github.com/chisangasage/note-taking-app',
        'featured': True,
        'order': 5,
    },
    {
        'title': 'Cartoon Hero Website',
        'description': 'A creative website showcasing cartoon heroes with interactive elements and responsive design.',
        'tech_stack': 'HTML, CSS, JavaScript',
        'github_link': 'https://github.com/chisangasage/cartoon-hero',
        'featured': True,
        'order': 6,
    },
]



for project_data in projects_data:
    Project.objects.create(**project_data)
"""
skills_data = [
    {'name': 'Python', 'category': 'Languages', 'proficiency': 95, 'icon': 'fab fa-python'},
    {'name': 'Django', 'category': 'web_dev', 'proficiency': 85, 'icon': 'fas fa-server'},
    {'name': 'Java', 'category': 'Languages', 'proficiency': 80, 'icon': 'fab fa-java'},
    {'name': 'Go', 'category': 'Languages', 'proficiency': 70, 'icon': 'fab fa-golang'},
    
    {'name': 'JavaScript', 'category': 'Languages', 'proficiency': 85, 'icon': 'fab fa-js'},
    {'name': 'HTML/CSS', 'category': 'web_dev', 'proficiency': 90, 'icon': 'fab fa-html5'},
    {'name': 'Bootstrap', 'category': 'web_dev', 'proficiency': 85, 'icon': 'fab fa-bootstrap'},
    {'name': 'React', 'category': 'web_dev', 'proficiency': 75, 'icon': 'fab fa-react'},
    
    {'name': 'MySQL', 'category': 'database', 'proficiency': 85, 'icon': 'fas fa-database'},
    {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 80, 'icon': 'fas fa-database'},
    {'name': 'SQLite', 'category': 'database', 'proficiency': 85, 'icon': 'fas fa-database'},
    
    {'name': 'Git', 'category': 'cloud_&_tools', 'proficiency': 85, 'icon': 'fab fa-git-alt'},
    {'name': 'Linux', 'category': 'cloud_&_tools', 'proficiency': 80, 'icon': 'fab fa-linux'},
    {'name': 'Docker', 'category': 'cloud_&_tools', 'proficiency': 70, 'icon': 'fab fa-docker'},
]

for skill_data in skills_data:
    Skill.objects.create(**skill_data)

print("Sample data added successfully!")
print(f"Created {Project.objects.count()} projects")
print(f"Created {Skill.objects.count()} skills")


CATEGORY_CHOICES = [
        ('Web Development', 'web_dev'),
        ('Programming Languages', 'Languages'),
        ('database management', 'Database'),
        ('Cloud & DevOps', 'cloud_&_tools'),
        ('AI/ML Tools', 'AI_&_ML'),
        ('Others Skills', 'Others_skills'),
    ]


"""