from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('update/<str:slug>/', BlogPostUpdate.as_view(), name="update"),
    path('create/', BlogPostCreate.as_view(), name="create"),
    path('<str:slug>/', BlogPostDetail.as_view(), name="detail"),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name="delete"),
]