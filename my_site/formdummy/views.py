from django.shortcuts import render
from django.views import View

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