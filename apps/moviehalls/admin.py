from django.contrib import admin

# Register your models here.
from apps.moviehalls.models import RedHall, BlueHall, BlackHall, Halls, Movies, Reserved

admin.site.register(RedHall)
admin.site.register(BlueHall)
admin.site.register(BlackHall)
admin.site.register(Halls)
admin.site.register(Movies)
admin.site.register(Reserved)
