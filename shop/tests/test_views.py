from django.test import TestCase, Client
from shop.views import PurchaseCreate
from shop.models import Product, Purchase, ProductToPurchase, ProductType


class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.type1 = ProductType.objects.create(name="tires")
        Product.objects.create(name="tires R16", price="1500", type=self.type1)
        Product.objects.create(name="tires R15", price="1450", type=self.type1)

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_buy_webpage(self):
        response = self.client.get('/buy/?product_id=7&product_id=8')
        self.assertEqual(response.status_code, 200)

    def test_buy_function(self):
        response = self.client.post('/buy/?product_id=7&product_id=8', {'products': '7,8', 'person': 'Ivanov',
                                                                        'address': 'Svetlaya St.'})
        self.assertEqual(response.status_code, 200)
