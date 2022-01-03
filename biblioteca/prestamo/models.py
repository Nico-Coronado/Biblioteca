from django.db import models
from django.db.models.signals import post_delete, post_save

from libro.models import Book
from users.models import User
from . managers import LoanManager

class Loan(models.Model):
    # ForeignKey para el user de la aplicacion users
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date =  models.DateField(auto_now_add=True)
    return_date = models.DateField()
    returned = models.BooleanField()

    objects = LoanManager()

    def __str__(self):
        return str(self.book) + " | " + str(self.reader)


def subtract_book_stock(sender, instance, **kwargs):
    instance.book.stock = instance.book.stock - 1
    return instance.book.save()

def add_book_stock(sender, instance, **kwargs):
    instance.book.stock = instance.book.stock + 1
    return instance.book.save()

post_save.connect(subtract_book_stock, sender=Loan)
post_delete.connect(add_book_stock, sender=Loan)