from django.contrib import admin

from apps.moviehalls.models import RedHall, BlueHall, BlackHall, Halls, Movies, Reserved
# Register your models here.

admin.site.register(RedHall)
admin.site.register(BlueHall)
admin.site.register(BlackHall)
admin.site.register(Halls)
admin.site.register(Movies)
admin.site.register(Reserved)
