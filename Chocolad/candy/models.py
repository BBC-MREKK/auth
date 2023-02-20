from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from allauth.account.signals import user_logged_in


class Candy(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


User = get_user_model()

def user_logged_in_receiver(request, user, **kwargs):
    print(request)
    print(user)

    user_logged_in.connect(user_logged_in_receiver, sender=User)
