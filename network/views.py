from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
import datetime
import json
from django.http import JsonResponse
from .models import *


def index(request):
    all_post=add_post_content.objects.all()
    current_user=User.objects.filter(pk=request.user.id).first()
    all_liked_post=like.objects.all()
    p = Paginator(all_post, 3)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    print("print obj",page_obj)
    page1 = p.page(1)
    print(page1.object_list)
    whoyouliked=[]
    try:  
        for i in all_liked_post:
            print("i.liked_user.id",i.liked_user.id)
            print('request.user.id',request.user.id)
            if i.liked_user.id == request.user.id:
                whoyouliked.append(i.liked_post.id)
                print(whoyouliked)
    except:
        whoyouliked=[]
    print(whoyouliked)
    return render(request, "network/index.html",{
        "all_posts":all_post,
        "whoyouliked":whoyouliked,
        "page_obj":page_obj
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def add_post(request):
    if request.method=="POST":
       item=add_post_content()
       #item.seller=request.user.username
       item.author=request.user.username
       item.date=datetime.date.today()
       item.time=datetime.datetime.now()
       item.content = request.POST.get("content")
       item.save()
       all_post=add_post_content.objects.all()
       return render(request, "network/index.html",{
            "all_posts":all_post
            }   )
     #  return render(request,"network/index.html")
    else:
        return render(request,"network/addpost.html")

def profile(request,user):
    user_we=User.objects.get(id=user)
    current_user=request.user.username
    current_user1=request.user.id
    post=add_post_content.objects.filter(author=current_user)
    follower= Follow.objects.filter(follower=user_we)
    following= Follow.objects.filter(following=user_we)
    checkFollow=following.filter(follower=User.objects.get(pk=current_user1))
    print(post)
    return render(request,"network/profile.html",{"current_user":current_user,"post":post,"follower":follower,"following":following})

def follow(request,user_id):
    current_user=User.objects.get(pk=request.user.id)
    Followers_id=User.objects.get(username=user_id)
    f=Follow(follower=Followers_id,following=current_user)
    f.save()
    return HttpResponseRedirect(reverse("index"))

def unfollow(request,user_id):
    current_user=User.objects.get(pk=request.user.id)
    Followers_id=User.objects.get(username=user_id)
    f=Follow.objects.get(follower=Followers_id,following=current_user)
    f.delete()
    return HttpResponseRedirect(reverse("index"))

def following(request):
    current_user=User.objects.get(pk=request.user.id)
    print(current_user)
    all_following_list=Follow.objects.filter(following=current_user)
    print("all_following_list",all_following_list)
    all_posts=add_post_content.objects.all().order_by('id').reverse()
    print(all_posts)
    follow_post=[]

    for post in all_posts:
        for person in all_following_list:
            hello=str(post.author)
            world=str(person.following)
            print(hello,world)
            print(hello == world)
            if hello != world:
                follow_post.append(post)
                print("follow_post",follow_post)
    return render(request,"network/following.html",{
        "postss":follow_post
    })
    
def addtolike(request,id):
    current_user=request.user.id
    userrr=User.objects.get(pk=current_user)
    liked_user=id
    liked_user_name=add_post_content.objects.get(id=liked_user)
    likkkkkeeee=like(liked_user=userrr,liked_post=liked_user_name)    
    likkkkkeeee.save()
    return JsonResponse({"message":"like removed"})

def removelike(request,id):
    userrr=User.objects.get(pk=request.user.id)
    liked_by_userr=add_post_content.objects.get(id=id)
    likkkeeee=like.objects.filter(liked_user=userrr,liked_post=liked_by_userr)
    likkkeeee.delete()
    return JsonResponse({"message":"like removed"})

def comment_post(request,id):
    pass


def profile_for_loop(request,user_id):
    user=request.user.username
    current_user1=request.user.id
    current_user=add_post_content.objects.get(id=user_id)
    var=current_user.author
    variiii=User.objects.get(username=var)
    post=add_post_content.objects.filter(id=user_id)
    follower= Follow.objects.filter(follower=variiii)
    following= Follow.objects.filter(following=variiii)
    all_posts=add_post_content.objects.all().order_by('id').reverse()
    print("all" , post)
    try:
        checkFollow=follower.filter(following=User.objects.get(pk=current_user1)).count()
        print(checkFollow)
        if checkFollow !=0:
            isFollowing=True
        else:
            print("else")
            isFollowing=False
    except:
        print("except")
        isFollowing=False
    
    return render(request,"network/profile.html",{"user__1":user,"current_user":current_user.author,"post":post,"follower":follower,"following":following,"isFollowing":isFollowing})


def edit(request,post_id):
    if request.method=="POST":
        data= json.loads(request.body)
        edit_post=add_post_content.objects.get(pk=post_id)
        edit_post.content=data["content"]
        edit_post.save()
        return JsonResponse({"message":"successfully","data":data["content"]})