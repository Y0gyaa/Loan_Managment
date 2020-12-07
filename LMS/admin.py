from django.contrib import admin
from .models import borrowers

class Agent_admin(admin.ModelAdmin):
    fields=['prefix','name','principal_amt',
    'date_of_borrowing','duration','int_rate','paid_amt'
    ]

admin.site.register(borrowers,Agent_admin)