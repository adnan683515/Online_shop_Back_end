from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from add_to_cart.models import Order
# Create your views here.




class PaymentView(APIView):
    
    def get(self,request,format=None):
        obj = Order.objects.get()
    
        
        