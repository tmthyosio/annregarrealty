from django.contrib import admin
from .models import Property, Subdivision, Developer, PropertyImage

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'subdivision', 'status', 'price')
    list_filter = ('status', 'subdivision')
    search_fields = ('title', 'complete_address', 'subdivision__name')

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email')
    search_fields = ('name',)
    
@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer')
    list_filter = ('developer',)
    search_fields = ('name',)

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image')