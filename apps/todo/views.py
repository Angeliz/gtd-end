from rest_framework.decorators import action
from rest_framework.response import Response
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

    @action(detail=False)
    def get_todo(self, request):
        """
        通过用户id和项目id获取todo
        todo/get_todo?user={id}
        todo/get_todo?project={project_id}
        """
        empty_order = ''
        if (request.query_params.get('project')!=None):
            empty_order = Todo.objects.filter(todo_in_project=request.query_params.get('project')).order_by(
                'todo_create_at')
        elif (request.query_params.get('user')!=None):
            empty_order = Todo.objects.filter(todo_user=int(request.query_params.get('user'))).order_by(
            'todo_create_at')
        serializer = self.get_serializer(empty_order, many=True)
        return Response(serializer.data)