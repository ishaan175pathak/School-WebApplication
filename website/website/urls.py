"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Design.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path("login/",login),
    path('logout/',Logout),
    path("classroom/faculty/<str:name>/",classroom_faculty),
    path("classroom/faculty/<str:name>/queries/",classroom_faculty_queries),
    path("classroom/faculty/<str:name>/notices/",notice),
    path("classroom/faculty/<str:name>/studentEnroll/",studentEnroll),
    path("classroom/faculty/<str:name>/generate assignment/",make_assignment),
    path("classroom/faculty/<str:name>/submission/",submission),
    path("classroom/faculty/<str:name>/link/",linkpost),
    path("classroom/hod/allotment/",allotment),
    path("classroom/hod/",hod),
    path("classroom/hod/queries/",queries),
    path("classroom/hod/faculty_signup/",facultyEnroll),
    path("classroom/hod/notice_view/",noticeView),
    path("classroom/student/<str:name>/",classroom_student),
    path("classroom/student/<str:name>/studentPage/",classroom_student_home),
    path("classroom/student/<str:name>/view links/",linkView),
    path("classroom/student/<int:pk>/<str:name>/",make_submission),
    path("classroom/student/<str:name>/fees/",fees),
    path("classroom/student/<str:name>/library/",library),
    path("delete query/<int:pk>/",queryDelete),
    path("fetch query/<str:name>/",queryFetch),
    path("fetch notice/",noticeget),
    path("delete notice/<int:pk>/",noticeDelete),
    path("message post/",messagePost),
    path("fetch message/",messageGet),
    path("view submission/<str:name>/",viewSubmission),
    path("about us/",aboutUs)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)