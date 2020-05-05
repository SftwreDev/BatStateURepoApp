from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.utils.decorators import method_decorator
from .decorators import department_required
from .models import Documents_File, LogBook, User
from .forms import UploadFileForm,CustomAuthenticationForm, LogBookForm, DepartmentSignUpForm, FileForm, LogbookForm
from .filters import FileSearch, LogBookSearch

from bootstrap_modal_forms.generic import(BSModalLoginView, BSModalDeleteView, BSModalCreateView, BSModalUpdateView, BSModalReadView)


class HomepageView(TemplateView):
    template_name = 'repoapp/home.html'

class QuestionView(ListView):
    model = Documents_File
    template_name = 'repoapp/homepage.html'
    context_object_name = 'files'
    ordering = ['types_of_record', ]

@method_decorator([login_required, department_required], name='dispatch')
class FileList(ListView):
    model = Documents_File
    template_name = 'repoapp/file_list.html'
    context_object_name = 'file'
    ordering = ['types_of_record',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FileSearch(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        departmentsignup = self.request.user.departmentsignup
        department = departmentsignup.department.values_list('pk', flat=True)
        queryset = Documents_File.objects.filter(department__in=department)
        return queryset

class UploadFile(CreateView):
    model = Documents_File
    form_class = UploadFileForm
    success_url = reverse_lazy("repository:file_list")
    template_name = 'repoapp/create.html'

def DetailFileView(request , file_id):
    obj = get_object_or_404(Documents_File, file_id=file_id)
    template_name = "repoapp/detail.html"
    context = {"detail" : obj}
    return render(request, template_name, context)


class FileDeleteView(DeleteView):
    model = Documents_File
    context_object_name = 'file'
    template_name = 'repoapp/confirm_delete.html'
    success_url = reverse_lazy('repository:home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('repository:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@method_decorator([login_required, department_required], name='dispatch')
class LogBookList(ListView):
    model = LogBook
    template_name = 'logbook/logbook_list.html'
    context_object_name = 'file'
    ordering = ['document_description',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = LogBookSearch(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        departmentsignup = self.request.user.departmentsignup
        department = departmentsignup.department.values_list('pk', flat=True)
        queryset = LogBook.objects.filter(forwarded_by__in=department)
        return queryset


def download(request):
    if request.method == "POST":
        code = DepartmentCode.objects.all()
        department = Documents_File.objects.all()

        if department.code == code:
            return render(request, 'repoapp/file_list.html')



class UpdateLogBookList(CreateView):
    model = LogBook
    form_class = LogBookForm
    success_url = reverse_lazy("repository:logbook_list")
    template_name = 'logbook/update_logbook.html'


class DepartmentSignup(CreateView):
    model = User
    form_class = DepartmentSignUpForm
    template_name = 'registration/signup_form.html'


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'is_authorized'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('repository:home')


class DocumentsUpdateView(UpdateView):
    model = Documents_File
    form_class = UploadFileForm
    template_name = 'repoapp/documents_update.html'
    success_url = reverse_lazy('repository:file_list')



class FileDeleteView(BSModalDeleteView):
    model = Documents_File
    template_name = 'repoapp/delete_file.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('repository:file_list')

class LogbookDeleteView(BSModalDeleteView):
    model = LogBook
    template_name = 'logbook/delete_file.html'
    success_message = 'Success: Logbook was deleted.'
    success_url = reverse_lazy('repository:logbook_list')



class FileUpload(BSModalCreateView):

    template_name = 'repoapp/upload_file.html'
    form_class = FileForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('repository:file_list')


class FileUpdate(BSModalUpdateView):
    model = Documents_File
    template_name = 'repoapp/file_update.html'
    form_class = FileForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('repository:file_list')

class LogbookUpdate(BSModalUpdateView):
    model = LogBook
    template_name = 'logbook/logbook_update.html'
    form_class = LogbookForm
    success_message = 'Success: Logbook was updated.'
    success_url = reverse_lazy('repository:logbook_list')

class CreateLogbook(BSModalCreateView):
    template_name = 'logbook/create_logbook.html'
    form_class = LogbookForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('repository:logbook_list')



class FileView(BSModalReadView):
    model = User
    template_name = 'registration/login.html'
    context_object_name = 'file'


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'repoapp/controlled.html'
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('repository:file_list'))



