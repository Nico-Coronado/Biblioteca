from django.views.generic import FormView, ListView, DetailView, DeleteView
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . forms import LoanForm, LoanFormReturned
from . models import Loan

import datetime

class LoanFormView(FormView):
    form_class = LoanForm
    success_url = reverse_lazy('loan_app:loan-list')

    def form_valid(self, form):
        user = self.request.user

        Loan.objects.create(
            reader = user,
            book = self.get_object(),
            returned = False
        )
        return super(LoanFormView, self).form_valid(form)

class LoanFormReturnedView(FormView):
    form_class = LoanFormReturned
    success_url = reverse_lazy('loan_app:loan-list')

    def form_valid(self, form):
        Loan.objects.filter(pk=self.get_object().id).update(
            return_date=datetime.datetime.today(),
            returned=True
            )
        return super(LoanFormReturnedView, self).form_valid(form)


class LoanListView(LoginRequiredMixin, ListView):
    model = Loan
    template_name = "loan/loan_list.html"
    context_object_name = 'list'
    login_url = reverse_lazy('book_app:list-book')

    def get_queryset(self):
        user = self.request.user
        queryset = super(LoanListView, self).get_queryset()
        queryset = Loan.objects.loanList(user)
        return queryset


class LoanDetailView(LoanFormReturnedView, DetailView):
    model = Loan
    template_name = "loan/loan_detail.html"
    context_object_name = 'loan'


