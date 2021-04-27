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
        contact_number = request.POST["t4"]
        gender = request.POST["gender"]
        group = request.POST["group"]

        try:
            fainting = request.POST['fainting']
        except:
            fainting = 0
        try:
            bruise = request.POST['bruise']
        except:
            bruise = 0
        try:
            vein = request.POST['vein']
        except:
            vein = 0

        dob = request.POST["dob"]
        total = request.POST["donations"]
        pic = (request.FILES["picture"])
        weight = request.POST["weight"]

        obj = Donors.objects.create(
            name=name, address=addr, contact_number=contact_number, gender=gender, group=group, dob=dob, total=total, pic=pic, weight=weight, fainting=fainting, bruise=bruise, vein=vein)

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
        contact_number = request.POST["t4"]
        gender = request.POST["gender"]
        group = request.POST["group"]
        dob = request.POST["dob"]
        pic = (request.FILES["picture"])
        weight = request.POST["weight"]

        try:
            fainting = request.POST['fainting']
        except:
            fainting = 0
        try:
            bruise = request.POST['bruise']
        except:
            bruise = 0
        try:
            vein = request.POST['vein']
        except:
            vein = 0

        obj = Donors.objects.get(pk=id)
        obj.name = name
        obj.address = addr
        obj.contact_number = contact_number
        obj.gender = gender
        obj.group = group
        obj.dob = dob
        obj.pic = pic
        obj.fainting = fainting
        obj.bruise = bruise
        obj.vein = vein
        obj.weight = weight

        obj.save()
        msg = "record updated"
        return render(request, 'result.html', {'msg': msg})

    elif button == "Delete":
        id = request.POST['t1']
        obj = Donors.objects.get(pk=id)
        obj.delete()
        msg = "record deleted"
        return render(request, 'result.html', {'msg': msg})
