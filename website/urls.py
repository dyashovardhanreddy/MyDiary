from django.urls import path
from . import views 
from .views import WriteDiary


urlpatterns = [
    path('',views.home,name='website-home'),
    path('diary',views.diary,name='website-diary'),
    path(r'^readdiary/(?P<diary_id>[0-9]+)$',views.ReadDiary,name='website-read-diary')
]
