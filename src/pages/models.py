from django.db import models
from django.conf import settings
from src.profiles.models import MyUser

# Create your models here.


class Friend(models.Model):
    users = models.ManyToManyField(MyUser)
    current_user = models.ForeignKey(MyUser, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        new_friend.save()
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        new_friend.save()
        friend.users.remove(new_friend)


class PageInfo(models.Model):
    the_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(null=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True)

    def __str__(self):
        return str(self.the_user)


class PostOnPage(models.Model):
    post = models.CharField(max_length=500, null=True)
    post_Img = models.ImageField(upload_to='post_images/', null=True)
    user = models.ForeignKey(MyUser, related_name="user", on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True, null=True)


class Message(models.Model):
    sender = models.ForeignKey(MyUser, related_name="sender", on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(MyUser, related_name="receiver", on_delete=models.CASCADE, null=True)
    msg_content = models.CharField(max_length=400, default=None)
    created_at = models.TimeField(auto_now=True)
