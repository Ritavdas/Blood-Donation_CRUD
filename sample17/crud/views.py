from django.shortcuts import render
from .models import Donors
# Create your views here.


def index(request):
    return render(request, 'index.html')


def emp(request):
    button = request.POST["b1"]
    if button == "Insert":
        name = request.POST["t2"]
        addr = request.POST["t3"]
        age = request.POST["t4"]
        gender = request.POST["gender"]
        group = request.POST["group"]
        try:
            bike = request.POST['bike']
        except:
            bike = 0
        try:
            car = request.POST['car']
        except:
            car = 0
        try:
            boat = request.POST['boat']
        except:
            boat = 0
        dob = request.POST["dob"]
        total = request.POST["donations"]
        pic = (request.FILES["picture"])
        vehicles = request.POST.getlist('vehicles')
        amount = request.POST["amount"]

        obj = Donors.objects.create(
            name=name, address=addr, age=age, gender=gender, group=group, dob=dob, total=total, pic=pic, amount=amount, bike=bike, car=car, boat=boat)

        msg = "Record Inserted"
        return render(request, 'result.html', {'msg': msg})

    elif button == "Select":
        id = request.POST['t1']
        obj = Donors.objects.get(pk=id)
        return render(request, 'result.html', {'obj': obj})

    elif button == "Update":

        id = request.POST["t1"]
        name = request.POST["t2"]
        addr = request.POST["t3"]
        age = request.POST["t4"]
        gender = request.POST["gender"]
        group = request.POST["group"]
        dob = request.POST["dob"]
        pic = (request.FILES["picture"])
        amount = request.POST["amount"]
        try:
            bike = request.POST['bike']
        except:
            bike = 0
        try:
            car = request.POST['car']
        except:
            car = 0
        try:
            boat = request.POST['boat']
        except:
            boat = 0

        obj = Donors.objects.get(pk=id)
        obj.name = name
        obj.address = addr
        obj.age = age
        obj.gender = gender
        obj.group = group
        obj.dob = dob
        obj.pic = pic
        obj.bike = bike
        obj.car = car
        obj.boat = boat

        obj.amount = amount

        obj.save()
        msg = "record updated"
        return render(request, 'result.html', {'msg': msg})

    elif button == "Delete":
        id = request.POST['t1']
        obj = Donors.objects.get(pk=id)
        obj.delete()
        msg = "record deleted"
        return render(request, 'result.html', {'msg': msg})
