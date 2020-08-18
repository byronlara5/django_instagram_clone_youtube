from django.urls import path
from direct.views import Inbox, UserSearch, Directs, NewConversation, SendDirect
urlpatterns = [
   	path('', Inbox, name='inbox'),
   	path('directs/<username>', Directs, name='directs'),
   	path('new/', UserSearch, name='usersearch'),
   	path('new/<username>', NewConversation, name='newconversation'),
   	path('send/', SendDirect, name='send_direct'),

]