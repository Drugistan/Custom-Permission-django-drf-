from django.contrib import admin
from .models import CustomUser, Role
# Register your models here.


# class StateAdmin(admin.ModelAdmin):
#     model = CustomUser
#     list_display = ['Username', 'Password', 'roles', 'created_at',]
  
#     def active(self, obj):
#         return obj.is_active == 1
  
#     active.boolean = True

# admin.site.register(CustomUser, StateAdmin)

# class StateAdmin(admin.ModelAdmin):
#     list_display = ('id')
  
#     def active(self, obj):
#         return obj.is_active == 1
  
#     active.boolean = True
# admin.site.register(Role, StateAdmin)


class CustomAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username', 'password', 'roles', 'created_at' )

admin.site.register(CustomUser, CustomAdmin)



class RoleAdmin(admin.ModelAdmin):
    model = Role
    list_display = ('id',)

admin.site.register(Role, RoleAdmin)