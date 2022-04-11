from django.urls import path
from django.conf import settings
from blog import views

app_name='blog'

urlpatterns = [
    # path('',views.home_blog,name='home')
    path('',views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
]
