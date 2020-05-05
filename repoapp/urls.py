from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'repository'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('signup/', views.DepartmentSignup.as_view(), name='signup'),
    path('file-list/', views.FileList.as_view(), name='file_list'),
    path('upload/', views.UploadFile.as_view(), name='upload_file'),
    path('homepage/documents/detail/<int:file_id>/', views.DetailFileView, name='file_detailview'),
    path('file-document/<int:pk>/delete/', views.FileDeleteView.as_view(), name='file_delete'),
    path('homepage-view/', views.HomepageView.as_view(), name='home'),
    path('documents/documents-update/<int:pk>/', views.DocumentsUpdateView.as_view(), name='file_update'),

    path('logbook-list/', views.LogBookList.as_view(), name='logbook_list'),
    path('update-logbook-list/', views.UpdateLogBookList.as_view(), name='update_logbook_list'),

    path('delete/<int:pk>', views.FileDeleteView.as_view(), name='delete_file'),
    path('upload-file/', views.FileUpload.as_view(), name='file_upload'),
    path('update-file/<int:pk>', views.FileUpdate.as_view(), name='update_file'),

    path('new-log-book-list/', views.CreateLogbook.as_view(), name='logbook_create'),
    path('file-view/<int:pk>', views.FileView.as_view(), name='file_view'),
    path("logbook/delete/<int:pk>/", views.LogbookDeleteView.as_view(), name='logbook-delete'),
    path('logbook/update-logbook/<int:pk>/', views.LogbookUpdate.as_view(), name='logbook-update'),
    path('login', views.CustomLoginView.as_view(), name='loginpage'),
]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
