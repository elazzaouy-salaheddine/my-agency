from django.contrib import admin
from . import models



@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'services', 'client')



