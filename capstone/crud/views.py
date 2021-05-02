from django.shortcuts import render
from .models import Donors

from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class EmpView(TemplateView):
    def post(self, request, *args, **kwargs):
        button = request.POST["b1"]
        if button == "Insert":
            id = request.POST["t1"]
            name = request.POST["t2"]
            addr = request.POST["t3"]
            zipcode = request.POST["t4"]
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

            obj = Donors.objects.create(id=id,
                                        name=name, address=addr, zipcode=zipcode, gender=gender, group=group, dob=dob, total=total, pic=pic, weight=weight, fainting=fainting, bruise=bruise, vein=vein)

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
            zipcode = request.POST["t4"]
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
            obj.zipcode = zipcode
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
