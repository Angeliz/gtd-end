from rest_framework import serializers

from projects.models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_id', 'projects_name', 'projects_info', 'projects_complete', 'projects_create_at', 'projects_update_at','projects_user')


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_id', 'projects_name', 'projects_info', 'projects_complete', 'projects_create_at', 'projects_update_at','projects_user')


class ProjectsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_id', 'projects_name', 'projects_info', 'projects_complete', 'projects_create_at', 'projects_update_at','projects_user')


class ProjectsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_name', 'projects_info', 'projects_complete')

    def update(self, instance, validated_data):
        instance.projects_content = validated_data.get('projects_content', instance.projects_content)
        instance.projects_in_project = validated_data.get('projects_in_project', instance.projects_in_project)
        instance.projects_tag = validated_data.get('projects_tag', instance.projects_tag)
        instance.projects_complete = validated_data.get('projects_complete', instance.projects_complete)
        instance.save()
        return instance


class ProjectsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_name', 'projects_info', 'projects_complete', 'projects_user')

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

