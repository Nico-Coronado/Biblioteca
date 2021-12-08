from typing import IO
from django.contrib import admin

from . models import *

admin.site.register(Loan)
