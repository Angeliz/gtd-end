import uuid

from django.db import models

# Create your models here.
from users.models import Users
from projects.models import Projects

class Todo(models.Model):
    todo_id = models.UUIDField(primary_key=True,
                               default=uuid.uuid4,
                               editable=False,
                               verbose_name='一个todo的id',
                               help_text='todo的唯一id，pk')

    todo_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    todo_in_project = models.ForeignKey(Projects, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='所属项目',
                                        help_text='一个todo所属的项目')

    todo_content = models.TextField(verbose_name="内容", help_text="todo的内容")

    todo_tag = models.TextField(verbose_name='标签', help_text='todo的标签', default='今天',)
    todo_complete = models.BooleanField(verbose_name='是否完成', help_text='todo是否被标记为完成', default=False)

    todo_create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间戳', help_text='todo创建的时间戳')
    todo_update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间戳', help_text='每次数据修改的时间戳')

