from rest_framework.viewsets import ModelViewSet

from todo.models import Todo

from todo.serializers import TodoCreateSerializer, TodoUpdateSerializer, TodoRetrieveSerializer, TodoSerializer, TodoListSerializer


class TodoViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, ModulePermission)
    queryset = Todo.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TodoListSerializer
        elif self.action == 'create':
            return TodoCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return TodoUpdateSerializer
        elif self.action == 'retrieve':
            return TodoRetrieveSerializer
        else:
            return TodoSerializer
