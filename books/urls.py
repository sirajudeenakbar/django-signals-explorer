from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('test1/',views.test1),
    path('test2/',views.test2),
    path('test3/',views.test3),
    path("run-test1/", views.run_test1, name="run_test1"),
]