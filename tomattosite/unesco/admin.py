from django.contrib import admin
from unesco.models import Site, States, Category, Region, Iso


admin.site.register(Site)
admin.site.register(States)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Iso)