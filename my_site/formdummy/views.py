from django.shortcuts import render

def formDummyView(request):
        return render(request,
                      template_name='formdummy/form.html',
                      context={'Text':'Hello all'},)
