from django.db import models


class Ticket(models.Model):

    BRANCH_CHOICES = [
        ('Niterói', 'Niterói'),
        ('Petrópolis', 'Petrópolis'),
        ('Rio das Ostras', 'Rio das Ostras'),
        ('Teresópolis', 'Teresópolis'),
        ('Centro de Reparos', 'Centro de Reparos'),
    ]

    id = models.AutoField(primary_key=True)
    name_user = models.CharField("Nome do Usuário", max_length=100)
    date = models.DateTimeField("Data", auto_now_add=True)
    branch = models.CharField("Filial", max_length=100, choices=BRANCH_CHOICES)
    subject_purchase = models.CharField("Assunto da Compra", max_length=200)
    description = models.CharField("Observação", blank=True, null=True, max_length=500)
    status_ticket = models.IntegerField(default=1, editable=True)
    reason_for_rejection = models.CharField("Motivo da Rejeição", max_length=200, blank=True, null=True)
    who_approved = models.CharField("Gestor que aprovou", max_length=100, blank=True, null=True)
    date_approved = models.DateTimeField("Data Aprovado", blank=True, null=True)

    def __str__(self):
        return self.subject_purchase


class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    description_quotes = models.CharField("Descrição", max_length=300, blank=True, null=True)
    status = models.IntegerField("Status", default=0, editable=False, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="quote_ticket", null=True, blank=True)
    value = models.FloatField("Valor", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cotações"

    def __str__(self):
        return self.description_quotes
