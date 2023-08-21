from django.contrib import admin
from .models import contact1

# Register your models here.

class adminmodels(admin.ModelAdmin):
    list_display=['first_name','last_name','email_id','phone_No','Subject','Message']


admin.site.register(contact1,adminmodels)