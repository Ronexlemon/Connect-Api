from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

route=DefaultRouter()
route.register("products",views.ProductsView)
urlpatterns = [
    path("",include(route.urls))]

