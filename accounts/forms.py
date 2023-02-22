from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms


User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,
                               max_length=20)
    password_2 = forms.CharField(widget=forms.PasswordInput,
                                 max_length=20)
    
    class Meta:
        model = User
        fields = ('username', 'email',)
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email exists')
        return email
    
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('username taken')
        return username
    
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_2')
        if password is not None and password != password_2:
            self.add_error('password_2', 'password does not match')
        return cleaned_data
    
    
    
class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,
                               max_length=20)
    password_2 = forms.CharField(widget=forms.PasswordInput,
                                 max_length=20,
                                 label='Confirm Password')
    
    class Meta:
        model = User
        fields = ('email',
                  'username',
                  )
        
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_2')
        if password is not None and password != password_2:
            self.add_error('password_2', 'password does not match')
        return cleaned_data
    
    
    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
        

class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField
    
    class Meta:
        model = User
        fields = ('email',
                  'username',
                  'password',
                  'active',
                  'staff',
                  'admin')
        
    def clean_password(self):
        return self.initial['password']