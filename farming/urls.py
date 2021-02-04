from django.urls import path
from . import views
from farming import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', user_views.update_profile, name='update_profile'),
    # path('admin/<id>', views.admin, name='admin'),
    # path('farmers/<id>', views.farmers, name='farmers'),
    # path('suppliers/<id>', views.suppliers, name='suppliers'),
    # path('aboutus/', views.aboutus, name='aboutus'),
    # path('services/', views.services, name='services'),
    # path('products/', views.products, name='products'),
    # path('comment/<int:id>/',views.comment,name='comment'),
    path('new_farmer/', views.new_farmer, name='new_farmer'),
    path('editfarmer/', views.edit_farmer, name='editfarmer'),
    path('new_farmer/', views.newfarmer, name='newfarmer'),
    path('post', views.post, name='post'),
    # path('farmpost/<id>', views.postfarm, name='farmpost'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                   document_root=settings.MEDIA_ROOT)