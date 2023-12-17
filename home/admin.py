from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Vote)

admin.site.register(models.Comment)


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('name','autor','count')
