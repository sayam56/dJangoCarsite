from django.shortcuts import render
from django.http import HttpResponse
from .models import CarType, Vehicle, LabGroupMembers, OrderVehicle
from django.shortcuts import render, get_object_or_404
from django.views import View


# Create your views here.
def homepage(request):
    cartype_list = CarType.objects.all().order_by('id')
    return render(request, 'carapp/homepage.html', {'cartype_list': cartype_list})
# yes, we are passing extra context variable 'cartype_list' to the template which contains a list of all the vehicles
# for all car type

# def homepage(request):
#     cartype_list = CarType.objects.all().order_by('id')
#     response = HttpResponse()
#     heading1 = '<p>' + 'Different Types of Cars:' + '</p>'
#     response.write(heading1)
#     for cartype in cartype_list:
#         para1 = '<p>' + str(cartype.id) + ': ' + str(cartype) + '</p>'
#         response.write(para1)
#     # displaying 10 cars in descending order
#     vehicles = Vehicle.objects.all().order_by('-car_price')[:10]
#     heading2 = '<p>' + 'Vehicle List Descending order of price:' + '</p>'
#     response.write(heading2)
#     for vehicle in vehicles:
#         para2 = '<p>' + str(vehicle.id) + ': ' + str(vehicle) + ': ' + str(vehicle.car_price) + '</p>'
#         response.write(para2)
#
#     return response


def aboutUs(request):
    return render(request, 'carapp/aboutUs.html')
# we didn't need to pass any variables using the context parameter


# this was changed for the lab viva
# def cardetail(request, cartype_no):
    # # get the cartype object by the cartype_no
    # # cartype = CarType.objects.get(id=cartype_no)
    # cartype = get_object_or_404(CarType, id=cartype_no)
    #
    # # get the queryset of vehicles that belong to that cartype
    # vehicles = Vehicle.objects.filter(car_type=cartype)
    # response = HttpResponse()
    # heading1 = '<p>' + 'Vehicles of ' + str(cartype) + ':' + '</p>'
    # response.write(heading1)
    #
    # for vehicle in vehicles:
    #     orders = OrderVehicle.objects.filter(vehicle=vehicle)
    #     for order in orders:
    #         para = '<p> buyer is: ' + str(order.buyer) + ', Vehicle name is: ' + str(order.vehicle) + '</p>'
    #         response.write(para)
    # return response

def cardetail(request, cartype_no):
    # get the cartype object by the cartype_no
    # cartype = CarType.objects.get(id=cartype_no)
    cartype = get_object_or_404(CarType, id=cartype_no)

    # get the queryset of vehicles that belong to that cartype
    vehicles = Vehicle.objects.filter(car_type=cartype)

    # response = HttpResponse()
    # heading1 = '<p>' + 'Vehicles of ' + str(cartype) + ':' + '</p>'
    # response.write(heading1)
    #
    # # iterate over the vehicles and write a paragraph with the vehicle id, name, and price
    # for vehicle in vehicles:
    #     para = '<p>' + str(vehicle.id) + ': ' + str(vehicle) + ' - Price: ' + str(vehicle.car_price) + '</p>'
    #     response.write(para)
    #
    # return response
    # create a context dictionary to pass to the template
    context = {
        'cartype': cartype,
        'vehicles': vehicles,
    }

    # render the template with the context
    return render(request, 'carapp/cardetail.html', {'context': context})


# This was done using the CBV
class LabGroupMembersView(View):
    def get(self, request):
        # Retrieving all the lab group members from the model
        members = LabGroupMembers.objects.all()

        # Creating a list for member details
        member_details = []
        for member in members:
            member_details.append({
                'first_name': member.first_name,
                'last_name': member.last_name,
                'semester': member.semester,
                'personal_page_link': member.personal_page_link,
            })

        # render the template with the context
        return render(request, 'carapp/lab_group_members.html', {'member_details': member_details})

# Differences noticed:
#
# 1. Method Separation: In CBV, we separate code based on HTTP methods, but FBV directly handles logic in the view
# function.
# 2. Class Based Approach: CBV extends built in `View` class and provides better organization.
# 3. URL Configuration: In urls.py for CBV we use `.as_view()` to complete the routing, whereas in FBV we can directly
# call the view function.


def info_display(request):
    favourite_food = 'pizza'
    hobby = 'singing'
    return render(request, 'carapp/info_template.html', {'favourite_food':favourite_food, 'hobby':hobby})
