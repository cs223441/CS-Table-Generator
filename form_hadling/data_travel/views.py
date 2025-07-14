from django.shortcuts import render
from django.http import HttpResponse 
from .models import D_travel
# Create your views here.

def D_travel_view(request):
    number = None
    table = None 

    if request.method == 'POST':
        number = request.POST.get('number')
        try:
            num = int(number)
            table = [{'input': num , 'multiplier': i ,'result': i*num} for i in range(1 , 11)]
        except (ValueError , TypeError):
            return HttpResponse("Please enter a valid number.")

    return render(request,'index.html', {'table': table,'number': number})
        