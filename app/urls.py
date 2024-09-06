from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'jobPortal'
urlpatterns = [
                
                  path('', views.joblist, name='joblist'),
                  path('joblist/', views.joblist, name='joblist'),
                  path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
                  path('jobsingle1/', views.jobsingle1, name='jobsingle1'),
                  path('jobsingle2/', views.jobsingle2, name='jobsingle2'),
                  path('jobsingle3/', views.jobsingle3, name='jobsingle3'),
                  path('jobsingle4/', views.jobsingle4, name='jobsingle4'),
                  path('jobsingle5/', views.jobsingle5, name='jobsingle5'),
                  path('index8/', views.index8, name='index8'),
              ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)