from django.urls import path

from .views import BlogTreeListView, create_blog_tree

urlpatterns = [
    path("", BlogTreeListView.as_view(), name="blog_view"),
    path("create/", create_blog_tree, name="blog_create"),
]
