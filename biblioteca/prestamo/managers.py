from django.db import models

class LoanManager(models.Manager):
    def loanList(self, user):
        a = self.filter(
            reader = user
        )
        return a