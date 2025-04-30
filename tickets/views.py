from tickets.forms import TicketForm, QuoteForm, QuoteFormSet
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from tickets.models import Ticket
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone


@method_decorator(login_required(login_url='login'), name='dispatch')
class TicketsListView(ListView):

    model = Ticket
    template_name = 'tickets.html'
    context_object_name = 'tickets'
    paginate_by = 6

    def get_queryset(self):
        tickets = super().get_queryset().order_by('-date')
        search = self.request.GET.get('search')
        branch = self.request.GET.get('branch')

        if search:
            tickets = tickets.filter(subject_purchase__icontains=search)

        if branch:
            tickets = tickets.filter(branch=branch)

        for ticket in tickets:
            quotes = ticket.quote_ticket.all()
            ticket.has_quotes = any(quote.description_quotes for quote in quotes)

        return tickets


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewTicketView(View):

    def get(self, request):
        ticket_form = TicketForm()
        quote_forms = [QuoteForm(prefix=str(i)) for i in range(3)]

        if "reason_for_rejection" in ticket_form.fields:
            del ticket_form.fields["reason_for_rejection"]

        return render(request, 'new_ticket.html', {
            'ticket_form': ticket_form,
            'quote_forms': quote_forms
        })

    def post(self, request):
        ticket_form = TicketForm(request.POST)
        quote_forms = [QuoteForm(request.POST, prefix=str(i)) for i in range(3)]

        if ticket_form.is_valid() and all(form.is_valid() for form in quote_forms):
            ticket = ticket_form.save()

            for form in quote_forms:
                quote = form.save(commit=False)
                quote.ticket = ticket
                quote.save()

            return redirect('tickets_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = self.object

        has_valid_quotes = ticket.quote_ticket.filter(description_quotes__isnull=False).exclude(description_quotes="").exists()
        context['has_valid_quotes'] = has_valid_quotes
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class TicketStatusUpdate(View):
    def post(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        selected_quote_id = request.POST.get("selected_quote")
        value_status_ticket = request.POST.get("status_ticket")

        if value_status_ticket:
            ticket.status_ticket = 0
            ticket.save()

        if selected_quote_id:
            ticket.quote_ticket.update(status=0)
            ticket.who_approved = request.user.username
            ticket.date_approved = timezone.now()
            ticket.save()

            selected_quote = get_object_or_404(ticket.quote_ticket, id=selected_quote_id)
            selected_quote.status = 1
            selected_quote.save()

        return HttpResponseRedirect(reverse('ticket_detail', kwargs={'pk': ticket.pk}))


@method_decorator(login_required(login_url='login'), name='dispatch')
class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_update.html'
    success_url = '/tickets/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['quote_formset'] = QuoteFormSet(self.request.POST, instance=self.object)
        else:
            context['quote_formset'] = QuoteFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        self.object = form.save()

        quote_formset = QuoteFormSet(self.request.POST, instance=self.object)

        print(quote_formset)

        if quote_formset.is_valid():
            quote_formset.instance = self.object
            quote_formset.save()

            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form, quote_formset=quote_formset))
