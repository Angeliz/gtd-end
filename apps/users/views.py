from rest_framework.viewsets import ModelViewSet

from users.models import Users

from users.serializers import UsersCreateSerializer, UsersUpdateSerializer, UsersRetrieveSerializer, UsersSerializer,\
    UsersListSerializer


class UsersViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, ModulePermission)
    queryset = Users.objects.order_by('user_id')

    def get_serializer_class(self):
        if self.action == 'list':
            return UsersListSerializer
        elif self.action == 'create':
            return UsersCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return UsersUpdateSerializer
        elif self.action == 'retrieve':
            return UsersRetrieveSerializer
        else:
            return UsersSerializer
