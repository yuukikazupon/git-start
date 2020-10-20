from django import forms
from .models import Memo

class PostForm(forms.ModelForm):
    class Meta:
        model=Memo
        fields=['content']
        widgets = {
            'content':forms.Textarea
        }

CHOICE_FIELD_RECODE_NUMBERS = (
    ('10', '10件'),
    ('15', '15件'),
    ('30', '30件'),
)
CHOICE_FIELD_NEW_OLD=[
    ("1","新着順"),
    ("2","古い順"),
]

class RecordNumberForm(forms.Form):
    record_number = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange':'submit(this.form)'}),
        choices=CHOICE_FIELD_RECODE_NUMBERS
    )

class NewOldForm(forms.Form):
    new_old=forms.ChoiceField(
        widget=forms.Select(attrs={'onchange':'submit(this.form)'}),
        choices=CHOICE_FIELD_NEW_OLD
    )
