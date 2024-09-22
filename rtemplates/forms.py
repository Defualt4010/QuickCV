from django import forms
from rtemplates.models import Resume

# Class for Taking Input From the user to Build the Resume
class ResumeDetails(forms.ModelForm):
    # college_pointers = forms.FloatField(widget=forms.TextInput(attrs={
    #     'class': 'form-control', 
    #     'placeholder': 'College Pointers...'
    # }))

    phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Your Phone No...'
    }))

    class Meta:
        model = Resume

        # fields = ['first_name', 'last_name', 'phone', 'email', 'about', 'college_name', 'college_start_year', 'college_start_year', 'college_end_year', 'college_activity', 'college_pointers']

        fields = ['first_name', 'last_name', 'email', 'phone', 'about', 'college_name', 'college_start_year', 'college_end_year']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'First Name...'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Last Name...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Email...'
            }),
            'about': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'About Your Self...'
            }),
            'college_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'College Name...'
            }),
            'college_start_year': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'College Start Year...',
                'type': 'date'
            }),
            'college_end_year': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'College End Year...',
                'type': 'date'
            }),
            'college_activity': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Any Activity in College...'
            }),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove 'required' attribute from college_name and other college-related fields

        self.fields['first_name'].required = False
        self.fields['phone'].required = False
        self.fields['last_name'].required = False
        self.fields['about'].required = False
        self.fields['college_name'].required = False
        self.fields['college_start_year'].required = False
        self.fields['college_end_year'].required = False
        # self.fields['college_activity'].required = False


# Form to Inout Optional Mail
class OptionMail(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Email to Send your Resume...'
        }))
