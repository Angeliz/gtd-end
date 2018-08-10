from rest_framework.viewsets import ModelViewSet

from projects.models import Projects

from projects.serializers import ProjectsCreateSerializer, ProjectsUpdateSerializer, ProjectsRetrieveSerializer, ProjectsSerializer, ProjectsListSerializer


class ProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, ModulePermission)
    queryset = Projects.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectsListSerializer
        elif self.action == 'create':
            return ProjectsCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return ProjectsUpdateSerializer
        elif self.action == 'retrieve':
            return ProjectsRetrieveSerializer
        else:
            return ProjectsSerializer
