from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.SubscriptionPlans),
admin.site.register(models.UserSubscriptions)