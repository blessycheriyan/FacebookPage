from django.contrib import admin

# Register your models here.

from facebookapp.models import user
admin.site.register(user)
from facebookapp.models import bussinesspage
admin.site.register(bussinesspage)
