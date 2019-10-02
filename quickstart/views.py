from rest_framework import views, response
from .serializers import VisitSerializerAPI, UserSerializerAPI
from .models import Visit
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.contrib.auth.models import User


class RegisterAPI(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return response.Response({'data':'send password, username and email. we send token on your email'})

    def post(self, request):
        user = UserSerializerAPI(data=request.data)
        if user.is_valid():
            user.save()
            token = Token.objects.create(user_id=User.objects.get(username=user.data['username'], password=user.data['password']).id)
            send_mail('Token', str(token.key), 'bkozlovsky@bk.ru', ['bkozlovsky@bk.ru'], fail_silently=False)
            return response.Response('done')
        return response.Response('Error')


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

