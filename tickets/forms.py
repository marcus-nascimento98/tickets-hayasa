from django import forms
from django.forms import inlineformset_factory
from tickets.models import Ticket, Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['description_quotes', 'value']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name_user', 'branch', 'subject_purchase', 'description', 'status_ticket', 'reason_for_rejection']
        exclude = ['status_ticket']


QuoteFormSet = inlineformset_factory(Ticket, Quote, form=QuoteForm, extra=0, can_delete=True)
