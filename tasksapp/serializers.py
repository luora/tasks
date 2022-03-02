
from tasksapp.models import Task, TaskImage
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework import serializers

class TaskImageSerializer(ModelSerializer):

    class Meta:
        model = TaskImage
        fields = ('image',)

    
    def create(self, validated_data):
        print("validated data. {}", validated_data)
        return super().create(validated_data)

    
    # def create(self, validated_data):
    #     images_data = self.context.get('view').request.FILES

    #     task_image = Task.objects.create(title = validated_data.get('title', 'image-task'))

    #     for image_data in images_data.values():
    #         TaskImage.objects.create(task=task_image, image = image_data)

    #     return task_image

        


class TaskSerializer(HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    images = TaskImageSerializer(source = 'taskimage_set', many = True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'user', 'images')

    
    def create(self, validated_data):
        print(type(validated_data))
        print(validated_data)
        images_data = self.context.get('view').request.FILES
        print(images_data)
        print(validated_data)

        images1 = validated_data.get('image1')
        print(images1)
        
        #task = Task.objects.create(**validated_data)
        # task = Task.objects.create(title=validated_data.get('title', 'no-title'),
        #                            user_id=1)
        task = Task.objects.create(**validated_data)

        for image_data in images_data.values():
            TaskImage.objects.create(task = task, image = image_data)


        return task


    def validate(self, attrs):
        errors = {}
        title = attrs.get('title')
        images = self.context.get('view').request.FILES

        # print(images)

        # if title is not None and images is not None:
        #     return attrs

        # if title is None:
        #     raise serializers.ValidationError("empty tweet")

        
        # if not images:
        #     raise serializers.ValidationError("empty image  tweet")


        # if title is None and images is None:
        #     raise serializers.ValidationError("empty tweet")

        
        if not title and not images:
            raise serializers.ValidationError("empty tweet")


        return attrs


        
