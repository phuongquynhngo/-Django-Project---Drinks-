from django.contrib import admin
#import model in the same directory
from .models import Drink

admin.site.register(Drink)