from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'type', 'method', 'date')
    list_filter = ('type', 'method', 'date')
    search_fields = ('user__username', 'amount', 'type', 'method')