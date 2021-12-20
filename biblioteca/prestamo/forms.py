from django import forms
from django.forms import HiddenInput

from . models import Loan

class LoanForm(forms.ModelForm):
    """Form definition for Loan."""

    class Meta:
        """Meta definition for Loanform."""

        model = Loan
        exclude = ('reader', 'book', 'loan_date', 'return_date', 'returned')
        widgets = {'reader': HiddenInput(),}

class LoanFormReturned(forms.Form):

    class Meta:
        model = Loan
        exclude = ('reader', 'book', 'loan_date', 'return_date', 'returned')
        widgets = {'reader': HiddenInput(), }
