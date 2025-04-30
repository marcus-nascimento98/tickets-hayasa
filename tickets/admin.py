from django.contrib import admin
from tickets.models import Ticket, Quote


class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 1
    fields = ('description_quotes', 'value',)
    can_delete = False


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'subject_purchase', 'branch', 'date')
    search_fields = ('name_user', 'date', 'branch', 'subject_purchase')
    inlines = [QuoteInline]


admin.site.register(Ticket, TicketAdmin)
