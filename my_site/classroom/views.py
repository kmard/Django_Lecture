from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView
from classroom.forms import ContactForm
from django.urls import reverse,reverse_lazy

from classroom.models import Teacher


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

class TeacherCreateView(CreateView):
    model = Teacher
    #model_form.html
    #.save()
    fields = '__all__'
    success_url = '/classroom/thanks/'

class TeacherListView(ListView):
    model = Teacher
    #model_list.html
    queryset = Teacher.objects.order_by('first_name')

    context_object_name = 'teacher_list'
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TeacherDetailView(DetailView):
    #model_detail.html
    model = Teacher
    #PK --> {{teacher}}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TeacherUpdateView(UpdateView):
    #Share model_form.html --- PK
    model = Teacher
    fields = ['first_name','last_name','subject']
    # template_name_suffix = '_update_form'

    success_url = reverse_lazy('classroom:list_teacher')