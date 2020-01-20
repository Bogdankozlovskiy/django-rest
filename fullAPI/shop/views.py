from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from shop.serializer import CarDetailSerializer, CarListSerializer
from shop.models import Car
#from shop.permission import IsOwnerOrReadOnly
from rest_framework.response import Response


class CarCreateView(CreateAPIView):
	serializer_class = CarDetailSerializer


class CarsListView(ListAPIView):
	serializer_class = CarListSerializer
	queryset = Car.objects.all()


class CarDetailView(RetrieveUpdateDestroyAPIView):
	serializer_class = CarDetailSerializer
	queryset = Car.objects.all()
