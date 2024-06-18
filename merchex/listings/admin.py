from django.contrib import admin

# Register your models here.
from listings.models import Band
from listings.models import Listing

class BandAdmin(admin.ModelAdmin):
  list_display = ('name', 'genre', 'year_formed')

class ListingAdmin(admin.ModelAdmin):
  list_display = ('title', 'band','types')

admin.site.register(Listing, ListingAdmin)
admin.site.register(Band, BandAdmin)