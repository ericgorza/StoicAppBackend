from django.contrib import admin
from .models import Filosofo, Phrases, Picture

# Register your models here.
admin.site.register(Filosofo)
admin.site.register(Phrases)
admin.site.register(Picture)