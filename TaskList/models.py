from django.db import models
from django.conf import settings
from django.utils import timezone
from Account.models import User
from django.db.models.signals import post_save


# Create your models here.
class ToDoList(models.Model):
    title        = models.CharField(max_length=120)
    description  = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now())
    due_date     = models.DateTimeField(default=timezone.now())
    completed    = models.BooleanField(default=False)
    Author       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def post_save_receiver(sender, instance, created, **kwargs):
        pass

    post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
