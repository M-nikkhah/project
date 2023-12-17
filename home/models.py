from django.db import models

# Create your models here.
from accounts.models import User
from django.urls import reverse





class Book(models.Model):

    name=models.CharField(max_length=200,verbose_name='اسم کتاب')
    autor=models.CharField(max_length=200,verbose_name='نویسنده')
    translator=models.CharField(max_length=200,null=True,verbose_name='مترجم')
    language=models.CharField(max_length=200,verbose_name='ربان کتاب')
    data_of_release=models.DateField(null=True,verbose_name='زمان انتشار')
    name_orginal=models.CharField(max_length=200,null=True,verbose_name='اسم اصلی کتاب')
    price=models.IntegerField(null=True,verbose_name='قیمت نسخه چاپی')
    category = models.CharField(max_length=50,verbose_name='ژانر')
    price_Electric=models.IntegerField(null=True,verbose_name='قیمت نسخه الکتریکی')
    slug=models.SlugField(unique=True)
    is_electric_available=models.BooleanField(verbose_name='موجودیت نسخه الکتریکی')
    is_printed_available=models.BooleanField(verbose_name='موجودیت نسخه چاپی')
    publisher=models.CharField(max_length=200,verbose_name='ناشر',null=True)
    image = models.ImageField(verbose_name='نصویر')
    description =models.TextField(verbose_name='توضیحات')
    count=models.IntegerField(verbose_name='تعداد موجودی',default=0)
    credits=models.IntegerField(verbose_name='تیراژ',null=True)
    print_series=models.CharField(max_length=30,verbose_name='نوبت چاپ',null=True)
    number_of_pages=models.IntegerField(verbose_name='تعداد صفحات')
    ISBN=models.IntegerField(verbose_name='شابک',null=True)
    slug = models.SlugField(unique=True)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name='کتاب '
    def __str__(self):
       return f'{self.name} + {self.autor} '

class Vote(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='uvote', verbose_name='کاربر')
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='uvote', verbose_name='کتاب')
    def __str__(self):
        return f'{self.user} برای کتاب {self.book} '
    class Meta :
        verbose_name='رای '

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ucomment', verbose_name='کاربر')
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='bcommmnt',verbose_name='کتاب')
    body=models.TextField(verbose_name='متن تظر')
    repley=models.ForeignKey('self',on_delete=models.CASCADE,related_name='recomment', blank=True, null=True,verbose_name='ریپلای')
    is_replay=models.BooleanField(default=False,verbose_name='ریپلای  نظر دیگری')
    class Meta :
        verbose_name='نظرات '
    def __str__(self):
        return f'{self.user } برای {self.book} '