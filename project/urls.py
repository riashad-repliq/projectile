from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #SWAGGER API
    path('api/schema/', SpectacularAPIView.as_view(), name = 'api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name = 'api-schema'), name = 'api-docs'),

    #ProjectAPPs
    path('api/user/', include('core.urls')),

    path('api/shop/', include('shop.rest.urls')),


]
