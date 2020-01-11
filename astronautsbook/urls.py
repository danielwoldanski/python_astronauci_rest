from django.urls import path
from rest_framework.routers import DefaultRouter

from astronauts import views as contacts_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from astronauts import api

router = DefaultRouter()
router.register(r'snippets', api.AstronautViewSet)

urlAPIpatterns = [
    path('astronaut/', api.AstronautList.as_view()),
    path('astronaut/<int:pk>/', api.AstronautDetail.as_view())
]

urlAPIpatterns = format_suffix_patterns(urlAPIpatterns)


urlpatterns = [
    path('', contacts_views.AstronautView.as_view(), name ='astronaut-view'),


] + urlAPIpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
