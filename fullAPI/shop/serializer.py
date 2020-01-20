from rest_framework.serializers import ModelSerializer
from shop.models import Car
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ("username", "id")


class CarDetailSerializer(ModelSerializer):
	class Meta:
		model = Car
		fields = "__all__"


class CarListSerializer(ModelSerializer):
	#user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	#email = serializers.Serializer(label="hello label", default="default email", required=False)#test
	user = UserSerializer()
	class Meta:
		model = Car
		fields = ("vin", "user")