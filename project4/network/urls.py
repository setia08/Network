
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addpost",views.add_post,name="addpost"),
    path("addlike/<int:id>",views.addtolike,name="addlike"),
    path("removelike/<int:id>",views.removelike,name="removelike"),
    path("comment/<int:id>",views.comment_post,name="comment_post"),
    path("profile/<str:user>",views.profile,name="profile"),
    path("profile_for_loop/<int:user_id>",views.profile_for_loop,name="profile_for_loop"),
    path("follow/<str:user_id>",views.follow,name="follow"),
    path("unfollow/<str:user_id>",views.unfollow,name="unfollow"),
    path("following",views.following,name="following"),
    path("edit/<int:post_id>",views.edit,name="edit")
]