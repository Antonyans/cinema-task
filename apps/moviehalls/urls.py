from django.urls import path

from apps.moviehalls import views

urlpatterns = [
    path('', views.home, name='home'),
    path('red_hall/', views.red_hall, name='red_hall'),
    path('blue_hall/', views.blue_hall, name='blue_hall'),
    path('black_hall/', views.black_hall, name='black_hall'),
    path('red_hall/view_red_hall_film_detail/<int:hall_id>/<int:id>/', views.view_red_hall_film_detail,
         name='view_red_hall_film_detail'),
    path('blue_hall/view_blue_hall_film_detail/<int:hall_id>/<int:id>/', views.view_blue_hall_film_detail,
         name='view_blue_hall_film_detail'),
    path('black_hall/view_black_hall_film_detail/<int:hall_id>/<int:id>/', views.view_black_hall_film_detail,
         name='view_black_hall_film_detail'),
    path('reserved/<int:hall_id>/<int:id>/<int:seat_value>', views.reserved, name='reserved'),

]
