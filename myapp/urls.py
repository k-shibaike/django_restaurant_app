from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('gourmet_guide/', include('gourmet_guide.urls')),
    path('', RedirectView.as_view(url='gourmet_guide/')),
]