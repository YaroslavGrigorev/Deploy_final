from rest_framework import serializers
from .models import Autor, Task, TaskTags


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTags
        fields = "__all__"
