from django.urls import path
from .views import PostsViews, PostDetailView
app_name = 'blog'


urlpatterns = [
    path('', PostsViews, name='posts'),
    path('<id>/', PostDetailView, name='postdetails' ),

]
