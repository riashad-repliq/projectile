from django.urls import path
from shop import views
urlpatterns = [
    path('shops/', views.ShopListView.as_view(), name='shops'),
    path('shop/<int:pk>', views.ManageShopView.as_view(), name='shops'),

    path('roles/', views.RoleListView.as_view(), name='roles'),
]
