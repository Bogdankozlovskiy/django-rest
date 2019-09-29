from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views, response
from .serializers import UserSerializer, GroupSerializer, VisitSerializer
from .models import Visit
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitViewSetAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        visits = Visit.objects.all()
        serializer_class = VisitSerializer(visits, many=True)
        return response.Response({'data':serializer_class.data})

