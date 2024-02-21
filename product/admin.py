from django.contrib import admin
from .models import Plant, Perennial, Annual, Shrub, Tree

admin.site.register(Plant)
admin.site.register(Perennial)
admin.site.register(Annual)
admin.site.register(Shrub)
admin.site.register(Tree)