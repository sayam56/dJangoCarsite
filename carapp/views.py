from django.shortcuts import render
from django.http import HttpResponse
from .models import CarType, Vehicle


# Create your views here.
def homepage(request):
    cartype_list = CarType.objects.all().order_by('id')
    response = HttpResponse()
    heading1 = '<p>' + 'Different Types of Cars:' + '</p>'
    response.write(heading1)
    for cartype in cartype_list:
        para1 = '<p>' + str(cartype.id) + ': ' + str(cartype) + '</p>'
        response.write(para1)

    vehicles = Vehicle.objects.all().order_by('-car_price')[:10]
    heading2 = '<p>' + 'Vehicle List Descending order of price:' + '</p>'
    response.write(heading2)
    for vehicle in vehicles:
        para2 = '<p>' + str(vehicle.id) + ': ' + str(vehicle) + ': ' + str(vehicle.car_price) + '</p>'
        response.write(para2)

    return response


def aboutUs(request):
    response = HttpResponse()
    heading1 = '<p>' + 'This is a car showroom' + '</p>'
    response.write(heading1)
    return response


def cardetail(request, cartype_no):
    # get the cartype object by the cartype_no
    cartype = CarType.objects.get(id=cartype_no)

    # get the queryset of vehicles that belong to that cartype
    vehicles = Vehicle.objects.filter(car_type=cartype)

    # create an HttpResponse object to return as the response
    response = HttpResponse()

    # write a heading with the cartype name
    heading1 = '<p>' + 'Vehicles of ' + str(cartype) + ':' + '</p>'
    response.write(heading1)

    # iterate over the vehicles and write a paragraph with the vehicle id, name, and price
    for vehicle in vehicles:
        para = '<p>' + str(vehicle.id) + ': ' + str(vehicle) + ': ' + str(vehicle.car_price) + '</p>'
        response.write(para)

    # return the response
    return response
