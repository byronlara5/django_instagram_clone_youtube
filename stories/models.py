from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from post.models import Follow

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Story(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_user')
	content = models.FileField(upload_to=user_directory_path)
	caption = models.TextField(max_length=50)
	expired = models.BooleanField(default=False)
	posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username

class StoryStream(models.Model):
	following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_following')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	story = models.ManyToManyField(Story, related_name='storiess')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.following.username + ' - ' + str(self.date)

	def add_post(sender, instance, *args, **kwargs):
		new_story = instance
		user = new_story.user
		followers = Follow.objects.all().filter(following=user)

		for follower in followers:
			try:
				s = StoryStream.objects.get(user=follower.follower, following=user)
			except StoryStream.DoesNotExist:
				s = StoryStream.objects.create(user=follower.follower, date=new_story.posted, following=user)
			s.story.add(new_story)
			s.save()

# Story Stream
post_save.connect(StoryStream.add_post, sender=Story)