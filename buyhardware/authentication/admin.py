from django.contrib import admin
from authentication.models import User, Client, Manager


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'email', 'phone_number', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('login', 'email', 'phone_number')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'legal_name', 'legal_address', 'postal_address', 'tin')
    search_fields = ('user_id', 'legal_name', 'legal_address', 'postal_address', 'tin')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'second_name', 'patronymic')
    search_fields = ('user_id', 'first_name', 'second_name', 'patronymic')
