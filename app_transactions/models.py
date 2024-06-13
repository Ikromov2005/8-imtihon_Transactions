from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('income', 'KIRIM +'),
        ('expense', 'CHIQIM -')
    ]
    METHOD_CHOICES = [
        ('card', 'Karta orqali'),
        ('cash', 'Naqd pul'),
        ('click', 'Click orqali')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miqdori")
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, verbose_name="Turi")
    method = models.CharField(max_length=5, choices=METHOD_CHOICES, verbose_name="Usuli")

    def str(self):
        return f"{self.amount} - {self.type} - {self.method}"