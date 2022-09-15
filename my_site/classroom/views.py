from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from classroom.forms import ContactForm
from django.urls import reverse,reverse_lazy


# Create your views here.
# https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#templateview

class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThanksView(TemplateView):
    template_name = 'classroom/thanks_page.html'

class ContactFormView(FormView):
    template_name = 'classroom/contact.html'
    form_class = ContactForm

    # success_url = '/classroom/thanks/'
    success_url = reverse_lazy('classroom:thanks1')


    def form_valid(self, form):
        print(form.cleaned_data)
        # {'name': 'Mike', 'message': '55'}
        return super().form_valid(form)

