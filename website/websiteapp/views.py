from django.shortcuts import render
from .models import places,team
# Create your views here.
def demo(request):
    ob=places.objects.all()
    ob1=team.objects.all()
    return render(request,'index.html',{'result':ob,'members':ob1})