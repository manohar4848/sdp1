from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.demofunction1, name="hel"),
    path('', views.homer, name="home"),
    path('about/', views.aboutfunction, name="about"),
    path('login/', views.loginfunction, name="login"),
    path('contact/', views.contactfunction, name="contact"),
    path('ad/', include("adminapp.urls")),  # Include adminapp.urls without 'a/' in the main urls
    path('adminhome.html', views.admin_home, name='admin_home'),
    path('facultylogin/', views.facultylogin, name="facultylogin"),
    path('studentlogin/', views.studentlogin, name="studentlogin"),
    path('st/', include("studentapp.urls")),
    path('fa/', include("facultyapp.urls")),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)