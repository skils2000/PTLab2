from django.test import TestCase
from shop.models import Product, Purchase, ProductToPurchase, ProductType
from datetime import datetime

class ProductTestCase(TestCase):
    def setUp(self):
        self.type1 = ProductType.objects.create(name="tires")
        self.type2 = ProductType.objects.create(name="oil")
        Product.objects.create(name="tires R16", price="1500", type=self.type1)
        Product.objects.create(name="motor oil X6", price="5000", type=self.type2)

    def test_correctness_types(self):
        self.assertIsInstance(Product.objects.get(name="tires R16").name, str)
        self.assertIsInstance(Product.objects.get(name="tires R16").price, int)
        self.assertIsInstance(Product.objects.get(name="tires R16").type, ProductType)
        self.assertIsInstance(Product.objects.get(name="motor oil X6").name, str)
        self.assertIsInstance(Product.objects.get(name="motor oil X6").price, int)
        self.assertIsInstance(Product.objects.get(name="motor oil X6").type, ProductType)

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="tires R16").price == 1500)
        self.assertTrue(Product.objects.get(name="motor oil X6").price == 5000)

        self.assertTrue(Product.objects.get(name="tires R16").type == self.type1)
        self.assertTrue(Product.objects.get(name="motor oil X6").type == self.type2)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.type1 = ProductType.objects.create(name="tires")
        self.product_tires = Product.objects.create(name="tires R15", price="14500", type=self.type1)
        self.datetime = datetime.now()
        self.purchase = Purchase.objects.create(person="Ivanov",
                                                address="Svetlaya St.")

        ProductToPurchase.objects.create(product=self.product_tires, purchase=self.purchase, finalPrice=self.product_tires.price)


    def test_correctness_types(self):
        self.assertIsInstance(ProductToPurchase.objects.get(product=self.product_tires).finalPrice, int)
        self.assertIsInstance(ProductToPurchase.objects.get(product=self.product_tires).product, Product)
        self.assertIsInstance(ProductToPurchase.objects.get(product=self.product_tires).purchase, Purchase)
        self.assertIsInstance(Purchase.objects.get(pk=self.purchase.pk).person, str)
        self.assertIsInstance(Purchase.objects.get(pk=self.purchase.pk).address, str)
        self.assertIsInstance(Purchase.objects.get(pk=self.purchase.pk).date, datetime)

    def test_correctness_data(self):
        self.assertTrue(ProductToPurchase.objects.get(product=self.product_tires).finalPrice == 14500)
        self.assertTrue(Purchase.objects.get(pk=self.purchase.pk).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(pk=self.purchase.pk).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(pk=self.purchase.pk).date.replace(microsecond=0) == \
            self.datetime.replace(microsecond=0))