from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import django_excel as excel
from django.shortcuts import render_to_response
import numpy as np
from datetime import datetime
from django.shortcuts import render
from .forms import employeesFORM
from .models import employees
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'folha/home.html')

@login_required
def employees_Data(request):
    if request.method == 'POST':
        form = employeesFORM(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render_to_response('folha/thankyou.html')
            #return HttpResponseRedirect('home.html')
    else:
        form = employeesFORM()
    return render(request, 'folha/employees.html', {'form': form})
