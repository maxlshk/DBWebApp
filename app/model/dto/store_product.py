class StoreProductDTO:
    def __init__(self, upc, upc_prom, id_product, selling_price, products_number, promotional_product):
        self.__upc = upc
        self.__upc_prom = upc_prom
        self.__id_product = id_product
        self.__selling_price = selling_price
        self.__products_number = products_number
        self.__promotional_product = promotional_product

    @property
    def upc(self):
        return self.__upc

    @property
    def upc_prom(self):
        return self.__upc_prom

    @property
    def id_product(self):
        return self.__id_product

    @property
    def selling_price(self):
        return self.__selling_price

    @property
    def products_number(self):
        return self.__products_number

    def set_products_number(self, products_number):
        self.__products_number = products_number

    @property
    def promotional_product(self):
        return self.__promotional_product

    def set_product_number(self, product_number):
        self.__products_number = product_number

    def serialize(self):
        return {
            'UPC': self.__upc,
            'UPC_Prom': self.__upc_prom,
            'Product_ID': self.__id_product,
            'Price': str(self.__selling_price),
            'Amount': self.__products_number,
            'Promotional_Product': self.__promotional_product
            # 'upc': self.__upc,
            # 'upc_prom': self.__upc_prom,
            # 'id_product': self.__id_product,
            # 'selling_price': self.__selling_price,
            # 'products_number': self.__products_number,
            # 'promotional_product': self.__promotional_product
        }
