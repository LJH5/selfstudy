from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     NATION_A = 'kr' # value값
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATIONS_CHOICES = {
#         (NATION_A, '한국'), #보이는 값
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     }
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        # 위젯은 DB와 아무런 관련이 없다
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,

            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.TextInput(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
                
            }
        )

    )
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title') 사용자의 입력을 받지않는 것