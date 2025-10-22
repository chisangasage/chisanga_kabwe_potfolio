from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated technologies")
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & Others'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=50, help_text="Proficiency level (0-100)")
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class")
    
    class Meta:
        ordering = ['category', '-proficiency']
    
    def __str__(self):
        return f"{self.name} ({self.category})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
