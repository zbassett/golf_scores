from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Course, Hole, Tee, Event, Round, Score


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


class TeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tee
        fields = '__all__'


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class RoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Round
        fields = '__all__'


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class EventScoreSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'player_id': instance.id,
            'player_first_name': instance.first_name,
            'player_last_name': instance.last_name,
            'score': instance.score__score__sum,
            'par_on_played_holes': instance.score__tee__hole__count,
            'score_to_par': instance.score__score__sum - instance.score__tee__hole__count,
            'through': instance.score__tee__hole__count,
        }