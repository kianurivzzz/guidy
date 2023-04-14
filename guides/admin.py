from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from .models import Guide

admin.site.register(Guide, MarkdownModelAdmin)
