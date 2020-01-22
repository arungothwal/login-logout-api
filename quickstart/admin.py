from django.contrib import admin
from .models import MyUser,Friend
from django.contrib.auth.models import Group

# Register your models here.



class MyUserAdmin(admin.ModelAdmin) :
    list_display = ('first_name', 'email','gender','is_staff','Address','phone_no')
    search_fields = ['Address','first_name','gender']
    list_per_page = 10

    #
    # def has_add_permission(self, request):
    #     return True
    #
    # def has_delete_permission(self, request, obj=None):
    #     return True


admin.site.register(Friend)


admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)
