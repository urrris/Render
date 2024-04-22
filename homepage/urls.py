from django.urls import path
from . import views
from mysite import settings
from django.conf.urls.static import static


urlpatterns = [path('', views.RegisterView.as_view(), name='register'),
               path('login/', views.LoginView.as_view(), name='login'),
               path('workspace/', views.WorkspaceView.as_view(), name='workspace')]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)