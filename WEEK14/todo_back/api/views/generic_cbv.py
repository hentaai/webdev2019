from api.models import Task, TaskList
from api.serializers import TaskListSerializer2, TaskSerializer2, UserSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from api.filters import TaskFilter

class TaskLists(generics.ListCreateAPIView):
    # queryset = TaskList.objects.all()
    # serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        print(self.request)
        return TaskList.objects.filter(created_by=self.request.user.id)

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        print(self.request)
        return TaskList.objects.filter(created_by=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    serializer_class = TaskListSerializer2


class Tasks(generics.ListCreateAPIView):

    serializer_class = TaskSerializer2
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TaskFilter

    # filterset_fields = ('id', 'name', 'status', 'task_list_id')
    search_fields = ('id', 'name', 'status')
    ordering_fields = ('id', 'name', 'status')

    def get_queryset(self):
        print(self.request.query_params)
        try:
            tasklist = TaskList.objects.filter(created_by=self.request.user.id).get(id = self.kwargs['pk'])
        except TaskList.DoesNotExist:
            return Http404

        queryset = tasklist.tasks.all()
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     queryset = queryset.filter(name=name)
        return queryset


    def perform_create(self, serializer):
        serializer.save()