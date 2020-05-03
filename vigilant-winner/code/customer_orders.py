import unittest


"""
Complexity: 
    runtime: O(n)
    space: O(1)
"""
def is_first_come_first_served(dine_in_orders, take_out_orders, served_orders):

    # total number of served order must be equal to dine_in_orders + take_out_orders
    if len(served_orders) != len(dine_in_orders) + len(take_out_orders):
        return False

    # check until all orders are check out
    while served_orders:
        last_served_order = served_orders.pop()

        if dine_in_orders and dine_in_orders[-1] == last_served_order:
            # remove last dine order, since its matches last served order
            dine_in_orders.pop()
        if take_out_orders and take_out_orders[-1] == last_served_order:
            # remove last take out order, since its matches last served order
            take_out_orders.pop()

    # served_orders, dine_in_orders, take_out_orders must be exhausted
    # in order to serve in first come first serve order.
    return served_orders == dine_in_orders == take_out_orders == []


class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main(verbosity=2)