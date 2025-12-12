from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import ProfileDetailView


urlpatterns = [

    path("", ProfileDetailView.as_view(), name="home"),

    path('admin/', admin.site.urls),

    # auth / accounts
    path("accounts/", include("user.urls")),

    path("skills/", include("skills.urls")),

    # profiles
    path("", include("profiles.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
