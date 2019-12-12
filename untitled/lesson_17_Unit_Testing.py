import logging

PIZZA_SMALL_SIZE = 0
PIZZA_BIG_SIZE = 1
PAYMENT_BY_CASH = 0
PAYMENT_BY_CARD = 1


logger = logging.getLogger(__name__)


class Pizza(object):
    """
        Object for keep information about pizza.
    """

    PIZZA_SIZE = {
        PIZZA_SMALL_SIZE: 'small size',
        PIZZA_BIG_SIZE: 'big size'
    }

    @property
    def pizza_size(self):
        return self.PIZZA_SIZE.get(self.size)

    def __init__(self, size):
        if self.PIZZA_SIZE.get(size):
            self.size = size
        else:
            raise TypeError("Wrong pizza size: {}".format(size))


class Order(object):
    """
        Object for keep information about user's order
        and implements methods for state machine transaction.
    """

    PAYMENT_METHOD = {
        PAYMENT_BY_CARD: 'card',
        PAYMENT_BY_CASH: 'cash',
    }

    @property
    def payment(self):
        return self.PAYMENT_METHOD.get(self.payment_method)

    def __init__(self):
        self.pizza = None
        self.payment_method = None
        self.confirmed = False

    def select_pizza(self, pizza_size):
        logger.debug("Set order pizza: {}".format(pizza_size))
        self.pizza = Pizza(pizza_size)

    def select_payment(self, payment_method):
        logger.debug("Set order payment_method: {}".format(payment_method))
        self.payment_method = payment_method

    def confirm_order(self, confirm):
        logger.debug("Set order confirm: {}".format(confirm))
        self.confirmed = confirm


class User(object):
    """
        Object for keep information about users and theirs orders
    """
    def __init__(self, user_id):
        self.id = user_id
        self.orders = []

    def __str__(self):
        return str(self.id)

    def get_last_order(self):
        if self.orders:
            return self.orders[-1]
        return None

    def can_create_order(self):
        """
            If user has not finished order return False,
            in another case return True
            :return:
        """
        last_order = self.get_last_order()
        if last_order and last_order.state not in ['success', 'canceled']:
            return False
        return True


