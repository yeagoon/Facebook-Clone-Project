from src.profiles.models import MyUser
from src.pages.models import PageInfo, Friend, PostOnPage, Message
from django.shortcuts import render
from django.contrib import messages
from .forms import ProfileInfoForm, PostInfoForm, SendMessageForm
from src.profiles.views import login_view

# Create your views here.


def home_view(request):
    people = MyUser.objects.exclude(id=request.user.id)
    posts = PostOnPage.objects.all()
    friends = Friend.objects.all()
    form = PostInfoForm()
    context = {'users': people, 'form': form, 'posts': posts, 'friends': friends}
    return render(request, "home.html", context)


def posts_view(request):
    if request.method == 'POST':
        form = PostInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        post_user = PostOnPage.objects.last()
        current_user = request.user
        post_user.user = current_user
        post_user.save()
    return home_view(request)


def create_profile_view(request):
    current_user = request.user
    if current_user.is_authenticated:
        pass
    else:
        messages.error(request, 'You have to login first')
        login_view(request)
    form = ProfileInfoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, "profileInfo.html", context)


def save_profile_view(request):

    profile_image = request.FILES['profile_image']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    current_user = request.user

    if PageInfo.objects.filter(the_user=current_user).exists():
        PageInfo.objects.filter(the_user=current_user).update(first_name=first_name, last_name=last_name, age=age, profile_image=profile_image)
    else:
        new_profile = PageInfo(first_name=first_name, last_name=last_name, age=age, the_user=current_user, profile_image=profile_image)
        new_profile.save()
    return my_profile_view(request)


def my_profile_view(request, pk=None):
    # if pk == -1:
    #     return create_profile_view(request)
    if pk:
        current_user = MyUser.objects.get(pk=pk)
    else:
        current_user = request.user
    if PageInfo.objects.filter(the_user=current_user).exists():
        current_page_info = PageInfo.objects.get(the_user=current_user)
        context = {
            'current_page_info': current_page_info,
        }
        return render(request, "profile.html", context)
    else:
        return create_profile_view(request)


def friends_page_view(request):
    friend, created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all()
    context = {'friends': friends}
    return render(request, "friendPage.html", context)


def del_friend_view(request, pk):
    del_friend = MyUser.objects.get(pk=pk)
    Friend.lose_friend(request.user, del_friend)
    return home_view(request)


def add_friend_view(request, pk):
    new_friend = MyUser.objects.get(pk=pk)
    Friend.make_friend(request.user, new_friend)
    return home_view(request)


def message_box_view(request, pk):
    msg_receiver = MyUser.objects.get(pk=pk)
    msg_sender = request.user
    form = SendMessageForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'sender': msg_sender,
        'receiver': msg_receiver,
    }
    return render(request, "messagePage.html", context)


def send_message_view(request, pk):
    if pk:
        msg_receiver = MyUser.objects.get(pk=pk)
    current_user = request.user
    msg_content = request.POST['msg_content']
    new_message = Message.objects.create(sender=current_user, receiver=msg_receiver, msg_content=msg_content)
    new_message.save()
    message_list = Message.objects.filter(sender=current_user)

    context = {
        'sender': current_user,
        'messages': message_list,
    }
    return render(request, "sentMessages.html", context)

