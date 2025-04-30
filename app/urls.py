from django.contrib import admin
from django.urls import path
from tickets.views import NewTicketView, TicketsListView, TicketDetailView, TicketStatusUpdate, TicketUpdateView
from accounts.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('tickets/', TicketsListView.as_view(), name='tickets_list'),
    path('new_ticket/', NewTicketView.as_view(), name='new_ticket'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('ticket/<int:pk>/status/', TicketStatusUpdate.as_view(), name='ticket_status'),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name='ticket_update'),
]
