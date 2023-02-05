from django.test import TestCase
from .models import Product

class ProductModelTestCase(TestCase):
  def setUp(self):
    Product.objects.create(
      url='https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06',
      title='SRPM Wayfarer Sunglasses',
      description='A stylish pair of wayfarer sunglasses from SRPM',
      price=999,
      mobile_number='9876543210'
    )

  def test_product_url(self):
    product = Product.objects.get(title='SRPM Wayfarer Sunglasses')
    self.assertEqual(product.url, 'https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06')

  def test_product_title(self):
    product = Product.objects.get(title='SRPM Wayfarer Sunglasses')
    self.assertEqual(product.title, 'SRPM Wayfarer Sunglasses')

  def test_product_description(self):
    product = Product.objects.get(title='SRPM Wayfarer Sunglasses')
    self.assertEqual(product.description, 'A stylish pair of wayfarer sunglasses from SRPM')

  def test_product_price(self):
    product = Product.objects.get(title='SRPM Wayfarer Sunglasses')
    self.assertEqual(product.price, 999)

  def test_product_mobile_number(self):
    product = Product.objects.get(title='SRPM Wayfarer Sunglasses')
    self.assertEqual(product.mobile_number, '9876543210')
