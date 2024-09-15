from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Authentication urls
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    #Blog posts urls
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_form'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_confirm_delete'),

    # Blog comments urls
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name="comment_form"),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name = 'edit_comment'),

    path('search/', views.search_posts, name='search_posts'),
]