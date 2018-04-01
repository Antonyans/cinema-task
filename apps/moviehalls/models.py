from django.db import models


# Create your models here.


class Movies(models.Model):
    movie_name = models.CharField(max_length=100, blank=False)
    movie_image = models.ImageField(upload_to='static/images/movieImages', blank=False)
    showtime = models.DateTimeField()

    def __str__(self):
        return self.movie_name


class Halls(models.Model):
    seats = models.IntegerField(default=0)
    movies_showing = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.movies_showing.movie_name,
                                     self.movies_showing.showtime,
                                     self.seats
                                     )


class RedHall(models.Model):
    movies_red_hall = models.ForeignKey(Halls, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(
            self.movies_red_hall.movies_showing.movie_name,
            self.movies_red_hall.seats,
            self.movies_red_hall.movies_showing.showtime
        )


class BlueHall(models.Model):
    movies_blue_hall = models.ForeignKey(Halls, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(
            self.movies_blue_hall.movies_showing.movie_name,
            self.movies_blue_hall.seats,
            self.movies_blue_hall.movies_showing.showtime
        )


class BlackHall(models.Model):
    movies_black_hall = models.ForeignKey(Halls, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(
            self.movies_black_hall.movies_showing.movie_name,
            self.movies_black_hall.seats,
            self.movies_black_hall.movies_showing.showtime
        )


class Reserved(models.Model):
    film = models.ForeignKey(Movies, on_delete=models.CASCADE)
    hall = models.ForeignKey(Halls, on_delete=models.CASCADE)
    seat = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.film,
                                          self.hall,
                                          self.film.movie_name,
                                          self.film.showtime,
                                          )
