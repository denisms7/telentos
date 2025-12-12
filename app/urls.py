from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import ProfileDetailView, HomeDetailView


urlpatterns = [

    path("", HomeDetailView.as_view(), name="index"),
    path("inicio/", ProfileDetailView.as_view(), name="home"),

    path('admin/', admin.site.urls),
    # auth / accounts
    path("accounts/", include("user.urls")),

    # profiles
    path("", include("profiles.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
