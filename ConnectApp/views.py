from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
def index(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())
def form(request):
    template = loader.get_template("form.html")
    return HttpResponse(template.render())
@csrf_protect
@csrf_exempt
def addproduct(request):
    name = request.POST["Name"]
    description = request.POST["Description"]
    url = request.POST["Url"]
    price = int(request.POST["Price"])
    product = Products(productName=name,productDescription=description,productPrice=price,productImageUrl=url)
    product.save()
    return HttpResponseRedirect(reverse('home'))