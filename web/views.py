from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
import requests
import logging
import json

logging.basicConfig(filename='Views.log', encoding='utf-8', level=logging.DEBUG)


# Create your views here.
class overview(View):
    def get(self, request):
        return render(request, 'overview.html')


class location(View):
    def get(self, request):
        try:
            result = requests.get("http://localhost:5000/getlocationdetails")
            logging.info("view result in get: %s", result)
            response = {}
            response['data'] = result.json()
            logging.info("view response in get: %s", response)
            return render(request, 'location.html', response)
        except Exception as e:
            logging.exception(e)
            return redirect('overview')

    def post(self, request):
        logging.info("location post")
        try:
            data = {
                "location_name": request.POST.get('location_name')
            }
            result = requests.post("http://localhost:5000/insertlocationdetails", json=data)
            return redirect('location')
        except Exception as e:
            logging.exception(e)
            return redirect('overview')


class product(View):
    def get(self, request):
        try:
            result = requests.get("http://localhost:5000/getproductdetails")
            logging.info("view result in get: %s", result)
            response = {}
            response['data'] = result.json()
            logging.info("view response in get: %s", response)
            return render(request, 'product.html', response)
        except Exception as e:
            logging.exception(e)
            return redirect('overview')

    def post(self, request):
        logging.info("product post")
        try:
            data = {
                "product_name": request.POST.get('product_name'),
                "quantity": request.POST.get('quantity')
            }
            result = requests.post("http://localhost:5000/insertproductdetails", json=data)
            return redirect('product')
        except Exception as e:
            logging.exception(e)
            return redirect('overview')

class delete(View):
    def post(self, request):
        logging.info("delete product")
        try:
            delete_data = json.loads(request.POST.get('req_data'))
            data = {}
            if delete_data.get('productId'):
                data['productId'] = delete_data.get('productId')
                result = requests.post("http://localhost:5000/deleteproductdetails", json=data)
            else:
                data['locationId'] = delete_data.get('locationId')
                result = requests.post("http://localhost:5000/deletelocationdetails", json=data)
            return redirect('product')
        except Exception as e:
            logging.exception(e)
            return redirect('overview')

class movement(View):
    def get(self, request):
        return render(request, 'movement.html')
