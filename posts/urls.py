from django.urls import path
from . import views

app_name="posts"
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("inquiry/",views.InquiryView.as_view(),name="inquiry"),
    path("post_list/",views.PostListView.as_view(),name="post_list"),
    path("post_detail/<int:pk>/",views.PostDetailView.as_view(),name="post_detail"),
    path("post_create/",views.PostCreateView.as_view(),name="post_create"),
    path("post_update/<int:pk>/",views.PostUpdateView.as_view(),name="post_update"),
    path("post_delete/<int:pk>/",views.PostDeleteView.as_view(),name="post_delete"),
    path("penguin/",views.PenguinView.as_view(),name="penguin")
]