from django.contrib import admin
from app.models import user_registration,todolist_info
# Register your models here.
admin.site.register(user_registration)
admin.site.register(todolist_info)
