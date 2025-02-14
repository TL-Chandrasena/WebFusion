from django.shortcuts import render, redirect
from datetime import datetime
from .forms import LogMessageForm
from django import forms
from .models import LogMessage
from django.views.generic import ListView
class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)  # NOTE: the trailing comma is required

class HomeListView(ListView):
    model = LogMessage

# def home(request):
#     message_list = LogMessage.objects.all().order_by('-log_date')[:5]  # Adjust as needed
#     context = {'message_list': message_list}
#     return render(request, 'home.html', context)
from django.shortcuts import render
from django.utils import timezone

def home(request):
    message_list = LogMessage.objects.all().order_by('-log_date')[:5]  # Adjust as needed
    
    current_time = timezone.now()  # Get the current time
    context = {
        'message_list': message_list,
        'current_time': current_time,
          # Add the current time to the context
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def log_message(request):
    if request.method == 'POST':
        form = LogMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.name = "RAGHAVA KAMI REDDY VASA"  # Ensure that name is defined
            message.class_field = "web system development"
            message.log_date = datetime.now()
            message.save()
            return redirect("home")  # Update "home" to your home view's name

    else:
        form = LogMessageForm()  # Instantiate a blank form for GET

    return render(request, 'log_message.html', {'form': form})


def delete_log_message(request, log_id):
    log_message = LogMessage.objects.get(id=log_id)
    log_message.delete()
    return redirect('home')
