from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    #SWAGGER API
    path('api/schema', SpectacularAPIView.as_view(), name = 'api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name = 'api-schema'), name = 'api-docs'),

    #ProjectAPPs
    path('api/v1', include('core.rest.urls')),

    path('api/v1', include('shop.rest.urls')),

    path('api/v1', include('product.rest.urls')),

    path('api/v1', include('cart.rest.urls')),


]
