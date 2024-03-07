import pytest

from main import Category
from main import Product


@pytest.fixture()
def object_category():
    return Category('револьверы', 'размер барабана', [3, 6, 9])

def test_category(object_category):
    assert object_category.title == 'револьверы'
    assert object_category.description == 'размер барабана'
    assert object_category.goods == [3, 6, 9]

@pytest.fixture()
def object_product():
    return Product('патроны', 'калибр', 1000.0, 30)

def test_product(object_product):
    assert object_product.title == 'патроны'
    assert object_product.description == 'калибр'
    assert object_product.price == 1000.0
    assert object_product.quantity == 30

def test_total():
    category = Category('револьверы', 'размер барабана', [3, 6, 9])
    assert Category.total_categories == 2
    assert Category.total_unique_products == 6