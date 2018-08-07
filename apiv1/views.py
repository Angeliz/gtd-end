from rest_framework.viewsets import ModelViewSet

from apiv1.models import Users

from apiv1.serializers import FileCreateSerializer, FileUpdateSerializer, FileRetrieveSerializer, FileSerializer, \
    FileListSerializer


class UsersViewset(ModelViewSet):
    # permission_classes = (IsAuthenticated, ModulePermission)
    queryset = Users.objects.order_by('user_id')

    def get_serializer_class(self):
        if self.action == 'list':
            return FileListSerializer
        elif self.action == 'create':
            return FileCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return FileUpdateSerializer
        elif self.action == 'retrieve':
            return FileRetrieveSerializer
        else:
            return FileSerializer
