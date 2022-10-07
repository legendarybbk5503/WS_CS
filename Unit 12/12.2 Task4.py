from itertools import product


class Order:
    def __init__(self, no, date):
        self._orderNumber = no
        self._orderDate = date
        self._productsOrdered = []
        self._noOfItemsOrdered = 0
        self._status = OrderStatus()

    def orderItem(self, product):
        self._productsOrdered.append(product)

    def getOrderStatus(self):
        return self._status._hasShipped
    def getOrderItemID(self, id):
        return self._productsOrdered[id-1]._ID
    def getOrderItemPrice(self, id):
        return self._productsOrdered[id-1]._price

class OrderStatus:
    def __init__(self):
        self._hasShipped = False

class Product:
    def __init__(self, ID, price):
        self._ID = ID
        self._price = price

def main():
    product1 = Product("beans", 0.45)
    product2 = Product("eggs", 1.25)

    myOrder = Order(1, "1/1/17")
    myOrder.orderItem(product1)
    myOrder.orderItem(product2)

    print(myOrder.getOrderStatus())
    print(myOrder.getOrderItemID(1))
    print(myOrder.getOrderItemPrice(1))

    print(myOrder.getOrderItemID(2))
    print(myOrder.getOrderItemPrice(2))

if __name__ == "__main__":
    main()