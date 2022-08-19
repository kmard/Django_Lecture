from django.shortcuts import render
from django.views import View
from .forms import DummyForm

class formDummyView(View):
    def get(self, request,*args, **kwargs):
        return render(request,'formdummy/form.html',{'nameForm':'Feedback form',})

# 'https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/'
    def post(self,request,*args, **kwargs):
        text = request.POST.get('text')
        grade = request.POST.get('grade')
        image = request.FILES.get('image')
        content = image.read()
        #rederict
        return render(request,'formdummy/form.html',{'nameForm':'Feedback form',})

class formDummy(View):
    def get(self, request,*args, **kwargs):
        form = DummyForm
        return render(request,'formdummy/formDummy.html',
                      {'nameForm':'Feedback form dummy',
                       'form':form,
                       })
    def post(self,request,*args, **kwargs):
        form = DummyForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request,'formdummy/formDummy.html',
                          {'nameForm':'form Dummy reply',
                           'context':context
                           })
        else:
          return render(request, 'formdummy/Error.html',{'error':form.errors['text'][0]})


