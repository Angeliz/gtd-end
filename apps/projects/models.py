import uuid

from django.db import models

# Create your models here.
from users.models import Users


class Projects(models.Model):
    projects_id = models.UUIDField(primary_key=True,
                               default=uuid.uuid4,
                               editable=False,
                               verbose_name='一个projects的id',
                               help_text='projects的唯一id，pk')

    projects_user = models.ForeignKey(Users, on_delete=models.CASCADE)

    projects_name = models.TextField(verbose_name="项目名", help_text="一个项目的项目名")
    projects_info = models.TextField(verbose_name='介绍', help_text='一个项目的介绍信息')
    projects_complete = models.BooleanField(verbose_name='是否完成', help_text='projects是否被标记为完成', default=False)

    projects_create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间戳', help_text='projects创建的时间戳')
    projects_update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间戳', help_text='每次数据修改的时间戳')

