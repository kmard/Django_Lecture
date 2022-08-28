from django.shortcuts import render


def example_view(request):

    return render(request, "my_templates/example1.html",{})

def variable_view(request):

    some_list = [1,2,3]
    some_dict = {'inside_key':'inside_value'}
    return render(request, "my_templates/variable.html",{'name':'variable.html',
                                                         'name1': 'variable',
                                                         'some_list': some_list,
                                                         'some_dict':some_dict,
                                                         })

def loops_view(request):
    some_list = [1, 2, 3]
    some_dict = {'inside_key': 'inside_value'}
    return render(request, "my_templates/loops.html",{'name':'loops.html',
                                                         'name1': 'variable',
                                                         'some_list': some_list,
                                                         'some_dict':some_dict,
                                                         })

def Bollean_view(request):
    some_list = [1, 2, 3]
    some_dict = {'inside_key': 'inside_value'}
    return render(request, "my_templates/boolean.html",{'name':'bollean.html',
                                                         'name1': 'variable',
                                                         'some_list': some_list,
                                                         'some_dict':some_dict,
                                                          'user_logged_in':True,
                                                         })

def exBase_view(request):

    return render(request, "my_templates/exBase.html",{})
