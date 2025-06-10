from django.urls import path
from rest_framework.routers import DefaultRouter

from products.views.views import index, about, product_details, cart_add, cart_detail, checkout
from products.views.product import ProductViewSet
from products.views.category import CategoryViewSet

app_name = "products"
router = DefaultRouter()
router.register(r"products", viewset=ProductViewSet)
router.register(r"category", viewset=CategoryViewSet)


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path("product/<int:product_id>/", product_details, name="product_details"),
    path("cart_add/<int:product_id>/", cart_add, name="cart_add"),
    path("cart_details/<int:product_id>/", cart_detail, name="cart_details"),
    path("checkout/", checkout, name="checkout"),
]


urlpatterns += router.urls