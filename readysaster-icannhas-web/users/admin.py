# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import User, LGU


class UserAdmin(AuthUserAdmin):
    create_form_class = UserCreationForm
    update_form_class = UserChangeForm


class LGUAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(LGU, LGUAdmin)
