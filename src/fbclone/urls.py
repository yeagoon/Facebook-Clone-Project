"""fbclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from src.pages.views import home_view, my_profile_view, create_profile_view, save_profile_view, add_friend_view, \
    del_friend_view, friends_page_view, message_box_view, send_message_view, posts_view
from src.profiles.views import sign_in_view, login_view, logout_view, authentication_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('profile/', my_profile_view, name='show_profile'),
    path('<int:pk>/profile/', my_profile_view, name='show_profile_pk'),
    path('profileInfo/', create_profile_view, name='info_create'),
    path('profileInfoSave/', save_profile_view, name='save_profile'),
    path('sign_in/', sign_in_view, name='sign_in'),
    path('login/', login_view, name='login'),
    path('authentication/', authentication_view, name='authentication'),
    path('log_out/', logout_view, name='logout'),
    path('<int:pk>/del_friend/', del_friend_view, name='remove'),
    path('<int:pk>/friend/', add_friend_view, name='add_friend'),
    path('friends/', friends_page_view, name='friends_page'),
    path('<int:pk>/message_send/', message_box_view, name='message_box'),
    path('<int:pk>/message_box', send_message_view, name='send_message'),
    path('Post/', posts_view, name='do_post'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
