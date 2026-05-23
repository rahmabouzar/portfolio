from django.db import models

class Skill(models.Model):
    CATEGORIES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools'),
    ]
    name     = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    level    = models.IntegerField()  # 1-100

    def __str__(self):
        return self.name

class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack  = models.JSONField()         # ["React", "Django"]
    github_url  = models.URLField(blank=True)
    live_url    = models.URLField(blank=True)
    image       = models.ImageField(upload_to='projects/', blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title     = models.CharField(max_length=300)
    slug      = models.SlugField(unique=True)
    content   = models.TextField()          # Markdown
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    name    = models.CharField(max_length=100)
    email   = models.EmailField()
    body    = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"