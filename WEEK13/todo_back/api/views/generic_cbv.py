from api.models import Task, TaskList
from api.serializers import TaskListSerializer2, TaskSerializer2, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2

