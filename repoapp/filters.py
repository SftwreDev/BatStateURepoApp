import django_filters


from .models import Documents_File, LogBook

class FileSearch(django_filters.FilterSet):
    class Meta:
        model = Documents_File
        fields = {'identification_label' :[ 'icontains']}



class LogBookSearch(django_filters.FilterSet):
    class Meta:
        model = LogBook
        fields = {'document_description' :[ 'icontains']}
