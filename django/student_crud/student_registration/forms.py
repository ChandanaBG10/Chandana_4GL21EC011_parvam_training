from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    hobbies = forms.MultipleChoiceField(
        choices = [
            ('sports', "Sports"),
            ('music', "Music"),
            ('singing', "Singing"),
            ('dancing', "Dancing"),
            ('reading', "Reading"),
            ('traveling', "Traveling"),
        ],
        widget=forms.CheckboxSelectMultiple(),
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':3,
            'placeholder': 'Enter the address',
            'class':'form-control'
        })
    )

    class Meta:
        model = Registration
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'age':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'usn':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your usn'}),
            'email_id':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email-id'}),
            'branch':forms.Select(attrs={'class': 'form-select', }),
            'sem':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your semester'}),
            'course':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your course'}),
            'gender':forms.RadioSelect(attrs={'class': 'form-check',}),
            'profile_image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'resume_pdf':forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }