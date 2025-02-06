from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index),
    path('cats/<slug:cat_slug>/', views.categories),
    path("archive/<year4:year>/", views.archive)
]