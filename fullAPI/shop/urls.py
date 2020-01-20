from django.urls import path
from shop import views


app_name = "car"
urlpatterns = [
	path("create/", views.CarCreateView.as_view(), name="Car"),
	path("show/", views.CarsListView.as_view(), name="show"),
	path("update/<int:pk>/", views.CarDetailView.as_view(), name="update"),
]