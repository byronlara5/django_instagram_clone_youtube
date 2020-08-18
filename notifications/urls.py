from django.urls import path
from notifications.views import ShowNOtifications, DeleteNotification


urlpatterns = [
   	path('', ShowNOtifications, name='show-notifications'),
   	path('<noti_id>/delete', DeleteNotification, name='delete-notification'),

]