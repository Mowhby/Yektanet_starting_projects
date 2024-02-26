from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewAds.as_view(), name='viewAds'),
    path('add_new_ad/', views.new_form, name="new_form"),
    path('ad/<id>/', views.Redirect_view.as_view()),
    path('show_ad_status/<id>/', views.Status_view.as_view())
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
