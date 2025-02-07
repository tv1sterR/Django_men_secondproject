from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cats/<slug:cat_slug>/', views.categories, name='cats'),
    path("archive/<year4:year>/", views.archive, name='archive')
]