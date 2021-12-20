from django.db import models

from libro.models import Book
from users.models import User
from . managers import LoanManager

class Loan(models.Model):
    # ForeignKey para el user de la aplicacion users
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date =  models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField()

    objects = LoanManager()

    def __str__(self):
        return str(self.book) + " | " + str(self.reader)
