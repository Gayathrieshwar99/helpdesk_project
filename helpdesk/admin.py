from django.contrib import admin
from .models import UserProfile, Ticket

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "is_staff_agent")
    search_fields = ("user__username", "user__email", "phone")

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "priority", "created_by", "assigned_to", "created_at")
    list_filter = ("status", "priority", "created_at")
    search_fields = ("title", "description", "created_by__username", "assigned_to__username")