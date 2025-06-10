import pytest

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from account.models import Profile
from products.models import Cart, Product, Category, CartItem


@pytest.mark.django_db
def test_product_model():
    category = Category.objects.create(
        name = "test_category"
    )
    
    products = Product.objects.create(
        name="test_product",
        category=category,
        nomenclature="test_nomeclature",
        price=100,
        discount=10 
    )
    assert products.discount_price == 90
    assert products.category.name == "test_category"
    

@pytest.mark.django_db
def test_cart_model_one_product(user, product):
    cart =  Cart.objects.create(
        cart=user.cart,
        product = product
    )
    
    assert cart.item.item.total == product.price * 10
    assert cart.total == product.price * 10
    assert user.cart.total == 180