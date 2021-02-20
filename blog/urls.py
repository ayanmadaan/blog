from django.urls import path
from . import views
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, posts_of_following_profiles
from userreg import views as user_views
from userreg.models import Profile


urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="blog-about"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('profile/', user_views.profile, name="profile"),
    path('feed/', views.posts_of_following_profiles, name='feed')
]

