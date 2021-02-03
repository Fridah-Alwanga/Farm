from django.urls import path
from . import views
from farming import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('admin/', views.admin, name='admin'),
    path('farmers/<id>', views.farmers, name='farmers'),
    path('suppliers/<id>', views.suppliers, name='suppliers')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                   document_root=settings.MEDIA_ROOT)