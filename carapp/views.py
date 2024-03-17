from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import CarType, Vehicle, LabGroupMembers, OrderVehicle, Buyer
from django.shortcuts import render, get_object_or_404
from django.views import View, generic
from .forms import SearchVehicleForm, OrderVehicleForm, SignupForm, SearchCartypeForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def homepage(request):
    request.session['views'] = request.session.get('views', 0) + 1
    cartype_list = CarType.objects.all().order_by('id')
    return render(request, 'carapp/homepage.html', {'cartype_list': cartype_list, 'views': request.session['views']})


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
    image = ''
    if request.method == 'POST':
        form = SearchCartypeForm(request.POST)
        if form.is_valid():
            car_type = form.cleaned_data['car_type']
            image = car_type.image
    else:
        form = SearchCartypeForm()

    return render(request, 'carapp/aboutUs.html', {'form': form, 'image': image})
    # return render(request, 'carapp/aboutUs.html')


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


# this was done for the lab
def info_display(request):
    favourite_food = 'pizza'
    hobby = 'singing'
    return render(request, 'carapp/info_template.html', {'favourite_food': favourite_food, 'hobby': hobby})


def vehicles(request):
    # Retrieve all vehicles from the database
    vehicles_list = Vehicle.objects.all().order_by('id')

    # Render the template with the list of vehicles
    return render(request, 'carapp/vehicles.html', {'vehicles_list': vehicles_list})


def orderhere(request):
    msg = ''
    vehiclelist = Vehicle.objects.all()
    if request.method == 'POST':
        form = OrderVehicleForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.num_ordered <= order.vehicle.inventory:
                order.vehicle.inventory -= order.num_ordered
                order.vehicle.save()
                order.save()
                msg = 'Your vehicle has been ordered'
            else:
                msg = 'We do not have sufficient stock to fill your order.'
                response = render(request, 'carapp/nosuccess_order.html', {'msg': msg})
                # set a cookie that expires in 60 seconds
                response.set_cookie('OrderPage', 'Could Not Order', max_age=60)
                return response
    else:
        form = OrderVehicleForm()
    response = render(request, 'carapp/orderhere.html', {'form': form, 'msg': msg, 'vehiclelist': vehiclelist})
    response.set_cookie('OrderPage', 'ordering', max_age=60)
    return response
    # return render(request, 'carapp/orderhere.html', {'form': form, 'msg': msg, 'vehiclelist': vehiclelist})


def vsearch(request):
    car_price = ''
    if request.method == 'POST':
        form = SearchVehicleForm(request.POST)
        if form.is_valid():
            selected_car = form.cleaned_data['car_name']
            car_price = selected_car.car_price
    else:
        form = SearchVehicleForm()

    return render(request, 'carapp/vsearch.html', {'form': form, 'car_price': car_price})


class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('carapp/login')  # After signing up, redirect to login page
    template_name = 'carapp/signup.html'


def login_here(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('carapp:homepage'))
            else:
                return HttpResponse('Your account is disabled')
        else:
            return HttpResponse('Login details are incorrect')
    else:
        return render(request, 'carapp/login_here.html')


@login_required
def logout_here(request):
    logout(request)
    return HttpResponseRedirect(reverse('carapp:homepage'))


@login_required
def list_of_orders(request):
    if Buyer.objects.filter(username=request.user.username).exists():  # check if the user is a buyer
        orders = OrderVehicle.objects.filter(buyer__username=request.user.username)  # get all orders placed by the user
        return render(request, 'carapp/list_of_orders.html', {'orders': orders})
    else:
        return render(request, 'carapp/list_of_orders.html', {'message': 'You are not registered'})