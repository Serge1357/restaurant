from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Dish
from .forms import UserReservationForm

# Create your views here.


def base(request):
    if request.method == "POST":
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect("/")

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    spesials = Dish.objects.filter(spesial=True)
    reservation = UserReservationForm()

    data = {'categories': categories,
            'dishes': dishes,
            'spesials': spesials,
            "reservation_form" : reservation,
            }

    return render(request, 'base.html', context=data)
    

