from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
import json
from django.http import JsonResponse
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from .schemas import REVIEW_SCHEMA
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Feedback


class formDummyView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'feedback/form.html', {'nameForm': 'Feedback form', })

    # 'https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/'
    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        grade = request.POST.get('grade')
        image = request.FILES.get('image')
        content = image.read()
        # rederict
        return render(request, 'feedback/form.html', {'nameForm': 'Feedback form', })


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    # 'https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/'
    model = Feedback
    fields = ['text', 'grade', 'subject']
    success_url = '/feedback/add'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# pip install jsonschema
# @method_decorator(csrf_exempt,name='dispatch')
class SchemaJsonView(View):

    # Imitation API

    def post(self, request, *args, **kwargs):
        try:
            document = json.loads(request.body)
            validate(document, REVIEW_SCHEMA)
            return JsonResponse(document, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class MarshView(View):

    # Imitation API

    def post(self, request, *args, **kwargs):
        try:
            document = json.loads(request.body)
            validate(document, REVIEW_SCHEMA)
            return JsonResponse(document, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)


class FeedbackListView(LoginRequiredMixin, ListView):
    # 'https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-display/#listview'
    model = Feedback
    paginate_by = 20

    def get_queryset(self):
        if self.request.user.is_staff:
            return Feedback.objects.all()
        else:
            return Feedback.objects.filter(author=self.request.user)
