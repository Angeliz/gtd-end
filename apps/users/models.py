import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField, ArrayField
# Create your models here.


class Users(AbstractUser):
    # user_id = models.UUIDField(primary_key=True,
    #                             default=uuid.uuid4,
    #                             editable=False,
    #                             verbose_name='用户的id',
    #                             help_text='用户的唯一id，pk')

    # user_name = models.TextField(verbose_name="用户名", help_text="用户名")
    # user_password = models.TextField(verbose_name='密码', help_text='密码')
    user_info = models.TextField(verbose_name='介绍', help_text='用户详细信息', blank=True)









