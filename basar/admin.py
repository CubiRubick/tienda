from django.contrib import admin
from basar.models import (User, personalinfo, productinfo, comments)
# Register your models here.
class useradmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register(User, useradmin)

class perinfoadmin(admin.ModelAdmin):
    class Meta:
        model = personalinfo

admin.site.register(personalinfo, perinfoadmin)

class prodinfoadmin(admin.ModelAdmin):
    class Meta:
        model = productinfo

admin.site.register(productinfo, prodinfoadmin)

class commentsadmin(admin.ModelAdmin):
    class Meta:
        model = comments

admin.site.register(comments, commentsadmin)
