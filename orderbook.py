class OrderBook:
    def __init__(self):
        book = {}

    def buy(self, order_id, price):
        #x = [order_id, price]
        #book.append(x)
        book[order_id]=price

    def sell(self, order_id):
        book.pop(order_id,None)

    def get_high_price(self):
        if len(book) == 0:
            return -1
        high=book[max(book, key=lambda i: book[i])]
        return high

book = OrderBook()

for line in sys.stdin:
    elements = line.split(' ')
    time_order = int(elements[0])
    type_order = elements[1]
    id_order = int(elements[2])
    price_order = None
    if len(elements) == 4:
        price_order = float(elements[3])

    if elements[1] == 'B':
        book.buy(int(elements[2]), price_order)
    elif elements[1] == 'S':
        book.sell(int(elements[2]))
    if float(book.get_high_price()).is_integer():
        print str(int(elements[0])),str(int(book.get_high_price()))
    else:
        print str(int(elements[0])),str(book.get_high_price())