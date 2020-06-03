from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from .forms import RegisterForm
from .model import Event, EventSubscription


def show_event_list(request):
   events = Event.objects.all()
   return render(request, 'list.html', {'events': events})


def event_info(request, event_id):
   event = Event.objects.get(pk=event_id)
   return render(request, 'event.html', {'event': event, 'subscription': EventSubscription()})


def control_errors(subscription):
   errors = []
   if subscription.email == '':
      errors.append('Email is required')
   else:
      try:
         if EventSubscription.objects.get(email=subscription.email).event == subscription.event:
            errors.append('Email already registered for this event')
            return errors
      except EventSubscription.DoesNotExist:
         pass

   if subscription.name == '':
      errors.append('Name is required')

   return errors

def register(request):
   form = RegisterForm(request.POST)
   try:
      event = Event.objects.get(pk=form.data['event'])
   except MultiValueDictKeyError:
      return render(request, '404.html')
   subscription = EventSubscription()
   subscription.event = event
   subscription.name = form.data['name']
   subscription.email = form.data['email']
   subscription.comment = form.data['comment']

   errors = control_errors(subscription)

   if len(errors) == 0:
      subscription.save()
      return render(request, 'success.html')

   return render(request, 'event.html', {'event': event, 'subscription': subscription, 'errors': errors})
