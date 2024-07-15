from django.contrib import admin

from .models import Autor, Task, TaskTags

admin.site.register(Autor)
admin.site.register(Task)
admin.site.register(TaskTags)
