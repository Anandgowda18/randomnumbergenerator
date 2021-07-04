from django.shortcuts import render

# Create your views here.
import random
def number(request):
    x = random.randint(1,100)
    return render(request,'first.html',{'x':x})