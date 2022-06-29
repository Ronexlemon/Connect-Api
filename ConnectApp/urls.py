from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

route=DefaultRouter()
route.register("products", views.ProductsView)
urlpatterns = [
    path("api/",include(route.urls)),
path("", views.index, name="home"),
path("home/form/", views.form, name="form"),
path("home/form/addproduct/", views.addproduct, name="addproduct")]


