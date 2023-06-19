from django.contrib import admin
from .models import Domain,Extension,Gateway,UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Domain)
admin.site.register(Extension)
admin.site.register(Gateway)