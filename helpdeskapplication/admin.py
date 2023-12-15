from django.contrib import admin

from .models import *

admin.site.register(Person)
admin.site.site_url = "/helpdeskapplication/login"