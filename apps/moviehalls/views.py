from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.moviehalls.models import RedHall, Reserved, BlueHall, BlackHall


def home(request):
    return render(request, 'index.html', locals())


def red_hall(request):
    movie = RedHall.objects.all()
    context = {'movie': movie}
    return render(request, 'halls/redhall.html', context)


def blue_hall(request):
    movie = BlueHall.objects.all()
    context = {'movie': movie}
    return render(request, 'halls/bluehall.html', context)


def black_hall(request):
    movie = BlackHall.objects.all()
    context = {'movie': movie}
    return render(request, 'halls/blackhall.html', context)


def view_red_hall_film_detail(request, hall_id, id):
    movie_id = id
    movie = RedHall.objects.filter(movies_red_hall_id=movie_id)
    reserved_seat = Reserved.objects.filter(film_id=hall_id, hall_id=id)
    context = {'movie': movie, "reserved_seat": reserved_seat, }
    return render(request, 'reserved_film.html', context, )


def view_blue_hall_film_detail(request, hall_id, id):
    movie_id = id
    movie = BlueHall.objects.filter(movies_blue_hall_id=movie_id)
    reserved_seat = Reserved.objects.filter(film_id=hall_id, hall_id=id)
    context = {'movie': movie, "reserved_seat": reserved_seat, }
    return render(request, 'reserved_film.html', context, )


def view_black_hall_film_detail(request, hall_id, id):
    movie_id = id
    movie = BlackHall.objects.filter(movies_black_hall_id=movie_id)
    reserved_seat = Reserved.objects.filter(film_id=hall_id, hall_id=id)
    context = {'movie': movie, "reserved_seat": reserved_seat, }
    return render(request, 'reserved_film.html', context, )


def reserved(request, hall_id, id, seat_value):
    hall_id = id
    movie_id = hall_id
    print('movie', movie_id, 'hall', hall_id)
    if Reserved.objects.filter(hall_id=hall_id, film_id=movie_id, seat=seat_value):
        return HttpResponse('seat_is_a_reserveted')
    else:
        reserved_seat = Reserved.objects.create(hall_id=movie_id, film_id=hall_id, seat=seat_value)
    return HttpResponse('reserved')
