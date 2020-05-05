from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Documents_File, LogBook, User, Department, User, DepartmentSignup
from django.db import transaction

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = Documents_File
        fields = ['types_of_record', 'is_controlled','identification_label','box_no','label','department','document_file', 'retention']

class LogBookForm(forms.ModelForm):
    class Meta:
        model = LogBook
        fields = '__all__'


        
class DepartmentSignUpForm(UserCreationForm):
    department = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_authorized = True
        user.save()
        departmentsignup = DepartmentSignup.objects.create(user=user)
        departmentsignup.department.add(*self.cleaned_data.get('department'))
        return user


class FileForm(BSModalForm):
    class Meta:
        model = Documents_File
        fields = ['types_of_record', 'is_controlled','identification_label','box_no','label','department','document_file', 'retention']



class LogbookForm(BSModalForm):
    class Meta:
        model = LogBook
        fields = '__all__'


class LoginForm(BSModalForm):
    class Meta:
        model = User
        fields = ['username', 'password']