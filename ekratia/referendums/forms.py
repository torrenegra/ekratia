from django import forms
from .models import Referendum
from ekratia.threads.models import Comment


class ReferendumForm(forms.ModelForm):
    """
    Referendum Model Form
    """
    class Meta:
        model = Referendum
        exclude = ('user', 'slug', 'title')

    def __init__(self, *args, **kwargs):
        super(ReferendumForm, self).__init__(*args, **kwargs)
        self.fields['text_remove_rules'].widget = forms.Textarea(
            attrs={'rows': '2', 'ng-model': 'text1', 'msd-elastic': '',
                   'maxlength': '1000', 'placeholder': ''})
        self.fields['text_add_rules'].widget = forms.Textarea(
            attrs={'rows': '2', 'ng-model': 'text2', 'msd-elastic': '',
                   'maxlength': '1000', 'placeholder': ''})


class ReferendumCommentForm(forms.ModelForm):
    """
    Comment Referendums Model Form
    """
    class Meta:
        model = Comment
        fields = ('content',)
