from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('todo_id', 'todo_content', 'todo_in_project', 'todo_tag', 'todo_complete', 'todo_create_at', 'todo_update_at','todo_user')


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('todo_id', 'todo_content', 'todo_in_project', 'todo_tag', 'todo_complete', 'todo_create_at', 'todo_update_at', 'todo_user')


class TodoRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('todo_id', 'todo_content',  'todo_complete', 'todo_user')


class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('todo_content', 'todo_in_project', 'todo_tag', 'todo_complete')

    def update(self, instance, validated_data):
        instance.todo_content = validated_data.get('todo_content', instance.todo_content)
        instance.todo_in_project = validated_data.get('todo_in_project', instance.todo_in_project)
        instance.todo_tag = validated_data.get('todo_tag', instance.todo_tag)
        instance.todo_complete = validated_data.get('todo_complete', instance.todo_complete)
        instance.save()
        return instance


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('todo_content', 'todo_in_project', 'todo_tag', 'todo_complete', 'todo_user')

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

