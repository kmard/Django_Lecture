from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thanks/', views.ThanksView.as_view(), name='thanks1'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('new_teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),
    path('teachers_list/', views.TeacherListView.as_view(), name='list_teacher'),
    path('teachers_detail/<int:pk>', views.TeacherDetailView.as_view(), name='detail_teacher'),
    path('teacher_update/<int:pk>', views.TeacherUpdateView.as_view(), name='update_teacher'),
    path('teacher_delete/<int:pk>', views.TeacherDeleteView.as_view(), name='delete_teacher'),

]
