from django.contrib import admin
from .models import *


# Register your models here.


class display(admin.ModelAdmin):
    list_display = ('title', 'link', 'approve')
    list_filter = ('approve',)
    search_fields = ('title',)


admin.site.register(ad, display, )
admin.site.register(click,)
admin.site.register(report_hourly,)
admin.site.register(report_daily,)
admin.site.register(view,)
