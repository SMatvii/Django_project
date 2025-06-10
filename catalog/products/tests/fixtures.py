import pytest
from products.models import Category, Product


@pytest.fixture
def product(category_fixtures):
    return Category.objects.create(name="test_category_fixtures")



@pytest.fixture
def create_products(category_fixtures):
    category =Category.objects.create(
        name = 'test-category'
    )
    product = Product.objects.create(
        name = 'test-product',
        category=category_fixtures.id,
        nomenclature = 'test-nomenclature',
        price = 100
    )
    return product

@pytest.fixture
def product_discount(category_fixtures):
    category = Category.objects.create(name="test_user")
    return Product.objects.create(
        name="test_product",
        category=category_fixtures.id,
        nomenclature="test_nomenclature",
        price=100,
        discount=20  
    )