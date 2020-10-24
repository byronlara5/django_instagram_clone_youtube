from django.urls import path
from stories.views import NewStory, ShowMedia

urlpatterns = [
	path('newstory/', NewStory, name='newstory'),
	path('showmedia/<stream_id>', ShowMedia, name='showmedia'),
]