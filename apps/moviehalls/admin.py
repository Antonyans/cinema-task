from django.contrib import admin

# Register your models here.
from apps.moviehalls.models import RedHall, BlueHall, BlackHall, Halls, Movies, Reserved


class HallsAdmin(admin.ModelAdmin):
    class Meta:
        fieldsets = ('movies_red_hall', 'movies_showing')
        model = RedHall

admin.site.register(RedHall, HallsAdmin)
admin.site.register(BlueHall)
admin.site.register(BlackHall)
admin.site.register(Halls)
admin.site.register(Movies)
admin.site.register(Reserved)
