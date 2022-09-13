from django import forms
from django.forms import ModelForm
from .models import Review_stars


class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", max_length=100)
    email = forms.EmailField(label="email")
    review = forms.CharField(label="Write your review here",
                             widget=forms.Textarea(attrs={'cols': '80', 'rows': '2','class':'myform'}))


class ReviewFormStars(ModelForm):
    class Meta:
        model = Review_stars
        # fields = ['first_name', 'last_name', 'stars']
        fields = '__all__'
        labels={'first_name':'YOUR FIRST NAME',
                'last_name':'YOUR SECOND NAME',
                'stars':'RATING'
        }
        error_messages={
            'stars':{
                'min_value':'Min star is 1',
                'mix_value': 'Max star is 10',
            },
        }