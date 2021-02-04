from django.contrib import admin
from django.contrib.auth.models import Group,User
# from admin_interface.models import Theme
from .models import *

admin.site.register(Product)
admin.site.register(Yuviproduct)
admin.site.unregister(Group)
admin.site.unregister(User)
#admin.site.unregister(Theme)
admin.site.site_title="Admin TECH"
admin.site.site_header="LOGIN TECH"
admin.site.index_title="Welcome to Tech Portal"