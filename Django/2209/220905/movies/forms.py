from django import forms

class MovieForm(forms.Form):
    genre_a = 'comidy'
    genre_b = 'action'
    genre_choices = [
        (genre_a, '코미디'),
        (genre_b, '액션'),
    ]
    title = forms.CharField(max_length=20)
    audience = forms.IntegerField()
    genre = forms.ChoiceField(choices=genre_choices)
    description = forms.CharField(widget=forms.Textarea)
    