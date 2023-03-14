from django.contrib import admin
from . import models


admin.site.site_header = "Plausiblity_OTP_Assignment"
admin.site.register(models.Customer)
