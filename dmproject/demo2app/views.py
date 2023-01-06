from django.http import HttpResponse
from django.shortcuts import render

from .models import Place


# Create your views here.


def index(request):
    dest1 = Place()
    dest1.name = 'Mumbai'
    dest1.desc = ' The city that never sleeps'
    dest1.img = 'mumbai.jpg'

    dest2 = Place()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Biriyani'
    dest2.img = 'hyderabad.jpg'

    dest3 = Place()
    dest3.name = 'Bali'
    dest3.desc = ' Beautiful city'
    dest3.img = 'bali.jpeg'

    dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests': dests})
