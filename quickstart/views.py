from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views, response
from .serializers import UserSerializer, GroupSerializer, VisitSerializer, VisitSerializerAPI
from .models import Visit
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitViewSetAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        #print(request.GET.get('data'))# по приколу
        visits = Visit.objects.all()
        serializer_class = VisitSerializerAPI(visits, many=True)
        return response.Response({'data':serializer_class.data})

    def post(self, request):
        visit = VisitSerializerAPI(data=request.data)
        if visit.is_valid():
            visit.save()
            return response.Response(200)
        return response.Response(201)

