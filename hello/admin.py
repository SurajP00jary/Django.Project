from django.contrib import admin
from django.contrib.admin.decorators import register

from hello.models import Customer, farmer, plant, plant_purchased, seed_purchased, seeds,Products

# Register your models here.
admin.site.register(farmer)
admin.site.register(plant)
admin.site.register(plant_purchased)
admin.site.register(seed_purchased)
admin.site.register(seeds)
admin.site.register(Products)
admin.site.register(Customer)




