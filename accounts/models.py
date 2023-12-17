from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=255, unique=True,verbose_name='ایمیل')
	phone_number = models.CharField(max_length=11, unique=True,verbose_name='شماره تلفن')
	full_name = models.CharField(max_length=100,verbose_name='اسم کامل')
	is_active = models.BooleanField(default=True,verbose_name='فعال ')
	is_admin = models.BooleanField(default=False,verbose_name='ادمین ')

	class Meta:
		verbose_name = 'کاربر'
	objects = UserManager()

	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = ['email', 'full_name']

	def __str__(self):
		return self.email

	@property
	def is_staff(self):
		return self.is_admin


class OtpCode(models.Model):
	phone_number = models.CharField(max_length=11, unique=True,verbose_name='شماره تلفن ')
	code = models.PositiveSmallIntegerField(verbose_name='کد تایید')
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.phone_number} - {self.code} - {self.created}'

	class Meta:
		verbose_name = 'کد تایید کاربرها'



