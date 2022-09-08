from django import forms


class DummyForm(forms.Form):
    text = forms.CharField(label='Feed back',
                           min_length=3,
                           max_length=100,
                           )

    grade = forms.IntegerField(label='grade', min_value=1, max_value=100)
    image = forms.FileField(label='Photo', required=False)

    # check validation
    def clean_text(self):
        if 'abc' not in self.cleaned_data['text']:
            raise forms.ValidationError('not abc')
