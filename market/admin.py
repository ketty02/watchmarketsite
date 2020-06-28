from django.contrib import admin
from market.models.watch import Watch
from market.models.type import Type, WatchType

# Register your models here.
admin.site.register(Type)
admin.site.register(Watch)
admin.site.register(WatchType)