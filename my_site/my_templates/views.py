from django.shortcuts import render

# Create your views here.
def example_view(request):
    #my_templates/templates/my_templates/example1.html
    return render(request, "my_templates/example1.html",{})

def variable_view(request):

    some_list = [1,2,3]
    some_dict = {'inside_key':'inside_value'}
    return render(request, "my_templates/variable.html",{'name':'variable.html',
                                                         'some_list': some_list,
                                                         'some_dict':some_dict,
                                                         })
