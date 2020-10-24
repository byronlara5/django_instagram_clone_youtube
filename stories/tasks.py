from celery import shared_task
from stories.models import Story, StoryStream

from datetime import datetime, timedelta


#Task to check the stories date
@shared_task
def CheckStoriesDate():
	exp_date = datetime.now() - timedelta(hours=1)
	old_stories = Story.objects.filter(posted__lt=exp_date)
	old_stories.update(expired=True)
	print("Stories updated")


#Task to Delete the stories marked as expired by the CheckStoriesDate task
@shared_task
def DeleteExpired():
	Story.objects.filter(expired=True).delete()
	StoryStream.objects.filter(story=None).delete()

