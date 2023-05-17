from django.contrib import admin
from django.contrib import admin
from .models import UserProgress
from .forms import UserProgressForm

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    form = UserProgressForm
    fields = ['user', 'course', 'module', 'lesson', 'progress']

