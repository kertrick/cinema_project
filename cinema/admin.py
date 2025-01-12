from django.contrib import admin
from .models import Movie, Session, Customer, Ticket, Staff

admin.site.register(Movie)
admin.site.register(Session)
admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(Staff)
