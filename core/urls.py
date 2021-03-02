from django.contrib import admin
from django.urls import path,include
from core import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ac/', include('accounts.urls')),
    path('sys/', include('security.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
