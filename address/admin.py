from django.contrib import admin
from .models import Address,Country,State,District,City

admin.site.register(Address)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)