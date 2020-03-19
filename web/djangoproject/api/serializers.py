from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Course, Hole


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class HoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hole
        fields = '__all__'