from django.contrib import admin
from .models import Skill, Project, BlogPost, Message

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ['title', 'created_at']
    search_fields = ['title']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'published', 'created_at']
    prepopulated_fields = {'slug': ('title',)}  

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display  = ['name', 'email', 'sent_at']
    readonly_fields = ['name', 'email', 'body', 'sent_at']

admin.site.register(Skill)