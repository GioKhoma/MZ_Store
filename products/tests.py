# from django.test import TestCase
# from .models import Product


# class ProductTestCase(TestCase):

#     def test_product_discount_calculation(self):

#         product = Product(name="ტესტი", price=100)

#         self.assertEqual(product.get_discounted_price(10), 90)

#         self.assertEqual(product.get_discounted_price(100), 0)


# from users.models import User

# from .models import Product, Cart


# # class CartTestCase(TestCase):

# #     def test_add_product_to_cart_and_update_quantity(self):

# #         # Create user
# #         user = User.objects.create(username="giorgi")

# #         # Create product
# #         product = Product.objects.create(
# #             name="ლეპტოპი",
# #             price=2000,
# #         )

# #         # Create cart
# #         cart = Cart.objects.create(user=user)

# #         # Refresh product from database
# #         product.refresh_from_db()

# #         # Calculate cart total
# #         cart_total = sum(
# #             item.total_price()
# #             for item in cart.items.all()
# #         )

# #         # Check total price
# #         self.assertEqual(cart_total, 4000)
