from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from phones import views as phones_views

urlpatterns = [
    path('health', phones_views.health),
    path('admin/', admin.site.urls),
    path('phones/', include('phones.urls')),
    path('', RedirectView.as_view(url='/phones/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
