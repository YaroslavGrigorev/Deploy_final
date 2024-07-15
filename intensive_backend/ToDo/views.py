from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from .models import Autor, Task, TaskTags
from .serializers import AutorSerializer, TaskSerializer, TagSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class AutorAPIView(APIView):

    def get(self, request):
        queryset = Autor.objects.all()
        serializer = AutorSerializer(queryset, many=True)
        return Response({'posts': serializer.data})

    def post(self, request):
        serializer = AutorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put is not defined"})

        try:
            instance = Autor.object.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = AutorSerializer(data=request, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method delete is not defined"})
        Autor.objects.filter(id=pk).delete()
        return Response({"post": "delete post " + str(pk)})


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )


class TagViewSet(viewsets.ViewSet):
    '''queryset = TaskTags.objects.all()
    serializer_class = TagSerializer'''

    def list(self, request):
        queryset = TaskTags.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response({'posts': serializer.data})

    def create(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put is not defined"})

        try:
            instance = TaskTags.object.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = TagSerializer(data=request, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method delete is not defined"})
        TaskTags.objects.filter(id=pk).delete()
        return Response({"post": "delete post " + str(pk)})

