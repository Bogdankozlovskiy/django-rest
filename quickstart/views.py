from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views, response
from .serializers import UserSerializer, GroupSerializer, VisitSerializer, VisitSerializerAPI
from .models import Visit
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail


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
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        #test
        token = Token.objects.get(user_id=1)
        print(token)
        send_mail('subjects', str(token), 'bkozlovsky@bk.ru', ['bkozlovsky@bk.ru'], fail_silently=False)
        #test
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

