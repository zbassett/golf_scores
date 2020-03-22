from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from api.serializers import UserSerializer, GroupSerializer, CourseSerializer, HoleSerializer, TeeSerializer, EventSerializer, RoundSerializer, ScoreSerializer, EventScoreSerializer
from api.models import Course, Hole, Tee, Event, Round, Score
from django.db.models import Avg, Max, Min, Count, Sum
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class HoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Hole.objects.all()
    serializer_class = HoleSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Tee.objects.all()
    serializer_class = TeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Round.objects.all()
    serializer_class = RoundSerializer
    permission_classes = [permissions.IsAuthenticated]


class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventScoreViewSet(viewsets.ViewSet):
    """
    A ViewSet to return scores for an event.
    """
    def list(self, request):
        return 'rew'


    def retrieve(self, request, pk=None):
        # print('in EventScoreViewSet.list')
        queryset = User.objects.annotate(Sum('score__score'), Sum('score__tee__hole__par'), Count('score__tee__hole'), Max('score__round')).filter(score__round__event=pk)
        serializer = EventScoreSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, event_pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=event_pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)