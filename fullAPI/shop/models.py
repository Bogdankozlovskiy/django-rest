from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
	vin = models.CharField(verbose_name="Vin", unique=True, db_index=True, max_length=64)
	color = models.CharField(verbose_name="Color", max_length=64)
	brand = models.CharField(verbose_name="Brand", max_length=64)
	CAR_TYPES = (
			(1, "Sedan"),
			(2, "Hethback"),
			(3, "universal"),
			(4, "Cupe"),
		)
	car_type = models.IntegerField(verbose_name="Car Type", choices=CAR_TYPES)
	user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)

	def __str__(self):
		return self.vin
# Create your models here.
