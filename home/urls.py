
from . import views
from django.urls import path


app_name='home'
urlpatterns = [
 path('',views.HomeView.as_view(),name='home'),
 path('detiles/<slug:slug>/',views.ProductDetailView.as_view(),name='detiles')
]