from rest_framework import serializers
from .models import Skill, Project, BlogPost, Message

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Project
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = BlogPost
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Message
        fields = ['name', 'email', 'body']