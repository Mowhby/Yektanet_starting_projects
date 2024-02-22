from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewAds, name='viewAds'),
    path('add/', views.new_form, name="new_form"),
    path('click/<id>/', views.Redirect_view.as_view())
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
