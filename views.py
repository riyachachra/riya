from django.shortcuts import render
from djuser.models import Users

def Showuser(request):
    resultsdisplay = Users.objects.all()
    return render(request, "Page1.html", {'Users': resultsdisplay})
