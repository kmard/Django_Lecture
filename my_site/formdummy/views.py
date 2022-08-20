
from django.shortcuts import render
from django.views import View
from .forms import DummyForm
import json
from django.http import JsonResponse
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from .schemas import REVIEW_SCHEMA

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

#pip install jsonschema
class SchemaJsonView(View):

   #Imitation API

    def post(self,request,*args, **kwargs):
        try:
            document = json.loads(request.body)
            validate(document,REVIEW_SCHEMA)
            return JsonResponse(document,status = 201)
        except json.JSONDecodeError:
            return  JsonResponse({'errors':'Invalid JSON'}, status = 400)
        except ValidationError as exc:
            return  JsonResponse({'errors':exc.message}, status = 400)

        # form = DummyForm(request.POST)
        # if form.is_valid():
        #     context = form.cleaned_data
        #     return render(request,'formdummy/formScheme.html',
        #                   {'nameForm':'form Scheme reply',
        #                    'context':context
        #                    })
        # else:
        #   return render(request, 'formdummy/Error.html',{'error':form.errors['text'][0]})