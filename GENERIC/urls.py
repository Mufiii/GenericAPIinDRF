
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentlist/',views.studentList.as_view()),
    # path('studentcreate/',views.studentCreate.as_view()),
    # path('studentretrieve/<int:pk>',views.studentRetrieve.as_view()),
    # path('studentupdate/<int:pk>',views.studentUpdate.as_view()),
    # path('studentdelete/<int:pk>',views.studentDestroy.as_view()),
    
    path('lcstudentapi/',views.LCStudentapi.as_view()),
    path('rudstudentapi/<int:pk>',views.RUDStudentapi.as_view()),
]
