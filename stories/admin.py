from django.contrib import admin

from stories.models import Story, StoryStream

# Register your models here.

admin.site.register(Story)
admin.site.register(StoryStream)