from django import forms
from .models import User

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        # help text
        self.fields['username'].help_text = None

        # disabled
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True
        self.fields['special_subscription'].disabled = True
        self.fields['is_author'].disabled = True
    
    class Meta:
        model = User
        fields = [
            'username', 'email',
            'first_name', 'last_name',
            'special_subscription', 'is_author',
        ]