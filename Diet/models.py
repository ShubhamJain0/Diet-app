from django.db import models
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseNotFound


# Create your models here.
User=settings.AUTH_USER_MODEL


class DietdataQuerySet(models.QuerySet):
	def search(self, query):

		lookup = (Q(Age__iexact=query))

		return self.filter(lookup)



class DietdataManager(models.Manager):
	def get_queryset(self):
		return DietdataQuerySet(self.model, using=self._db)


	def search(self, query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)


	






class Dietdata(models.Model):

	Age = models.IntegerField(null=True)
	Deficiency = models.CharField(max_length=100)
	Quantity=models.IntegerField(null=True)
	Food=models.TextField(null=True)
	Meals_per_day=models.IntegerField(null=True)
	Time=models.IntegerField(null=True)
	user=models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	query=models.CharField(null=True, max_length=200)
	





	objects=DietdataManager()
	


