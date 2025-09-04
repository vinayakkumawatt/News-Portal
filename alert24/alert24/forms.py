from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=
    {'class':'form-control m-2 me-5 p-2  ',
     'placeholder':'Enter your name ',
     }))
    comment = forms.CharField(widget=forms.Textarea(attrs=
    {
        'class': 'form-control m-2 p-2',
        'placeholder':'Enter your comment here',
        'rows' : '5'
    }))